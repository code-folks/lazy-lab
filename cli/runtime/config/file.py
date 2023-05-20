import pydantic
import pathlib
import typing as t

from pydantic import tools, fields


from operator import attrgetter

S = t.TypeVar('S', bound=pydantic.BaseModel)


class ConfigFileError(Exception):
    pass


class ConfigValueError(ConfigFileError):
    pass


class ConfigFile(t.Generic[S]):

    DEFAULT_JSON_INDENT = 4

    def __init__(self, file: pathlib.Path, schema: t.Type[S], default: t.Optional[pathlib.Path] = None) -> None:
        self.file = file
        self.schema = schema
        self._default = default
        self._config_object = None
        self._create(force=False)

    @property
    def raw_object(self) -> S:
        """ TRY NOT USING THIS, this is direct access to the config on the disc. 
        Instead focus on accesing the cfg.config_object when readign the config as model.
        """
        try:
            return self.schema.parse_file(self.file)
        except pydantic.ValidationError as err:
            pretty_errors = pydantic.error_wrappers.display_errors(
                err.errors())
            raise ConfigFileError(
                f"Config file: {self.file}. Seems to be corrupted, fix errors:\n {pretty_errors}"
            )

    @property
    def config_object(self) -> S:
        if self._config_object is None:
            self._config_object = self.raw_object
        return self._config_object

    # Shorter alias for config_object
    data = config_object

    @property
    def default_config(self) -> S:
        if self._default is not None and self._default.exists():
            return self.schema.parse_file(self._default)
        return self.schema()

    def _create(self, force: bool = False) -> None:
        if self.file.exists() and not force:
            return
        if not self.file.exists():
            self._config_object = self.default_config
            return
        self.file.write_text(self.default_config.json())

    def _save(self) -> None:
        cfg = self.config_object.json(indent=ConfigFile.DEFAULT_JSON_INDENT)
        if not self.file.exists():
            self.file.parent.mkdir(parents=True, exist_ok=True)
            self.file.touch()
        self.file.write_text(cfg)

    def _reload(self):
        self._config_object = self.raw_object

    def _set_with_cast(self, target: pydantic.BaseModel, attr: str, value: t.Any) -> t.Any:
        if not isinstance(target, pydantic.BaseModel):
            raise RuntimeError("The config model is corrupted")
        model_fields: t.Dict[str, fields.ModelField] = getattr(
            target, "__fields__")
        field_definition: fields.ModelField = model_fields[attr]
        try:
            setattr(target, attr, tools.parse_obj_as(
                field_definition.outer_type_, value))
        except pydantic.ValidationError as e:
            error = e.errors().pop()
            raise ConfigValueError(f"Cannot assign `{value}` {error['msg']}")

    def set(self, key: str, value: t.Any, autosave: bool = True) -> None:
        nested_config, _, attr = key.rpartition(".")
        target = self.config_object
        nested_getter = attrgetter(nested_config)
        try:
            if nested_config:
                target = nested_getter(target)
            if isinstance(getattr(target, attr), pydantic.BaseModel):
                raise ConfigFileError("Cannot configure that.")
            self._set_with_cast(target, attr, value)
        except (AttributeError, KeyError):
            raise ConfigFileError(f"There is no `{key}` config property.")
        if autosave:
            self._save()

    def append(self, key: str, value: t.Any, autosave: bool = True) -> None:
        target_obj: t.Any = self.get(key)
        if not isinstance(target_obj, t.List):
            raise ConfigFileError(
                f"Target config property `{key}` is not appendable.")
        target_obj.append(value)
        if autosave:
            self._save()

    def remove(self, key: str, value: t.Any, autosave: bool = True) -> None:
        target_obj: t.Any = self.get(key)
        if not isinstance(target_obj, t.List):
            raise ConfigFileError(
                f"Target config property `{key}` is not a collection.")
        target_obj.remove(value)
        if autosave:
            self._save()

    def get(self, key: str) -> t.Any:
        value_getter = attrgetter(key)
        try:
            val = value_getter(self.config_object)
            if isinstance(val, pydantic.BaseModel):
                val = val.dict()
            return val
        except AttributeError:
            raise ConfigFileError(f"There is no `{key}` config property.")

    def restore(self) -> None:
        self._config_object = self.default_config
        self._save()

    def restore_key(self, key: str) -> None:
        value_getter = attrgetter(key)
        default_value = value_getter(self.default_config)
        self.set(key, default_value)

    def preview_full(self) -> dict:
        """ 
        Readonly full preview of the config data, any 
        change to the dict won't affect the config. 
        """
        return self.config_object.dict()
