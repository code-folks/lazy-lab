import pydantic
import pathlib
import typing as t

from operator import attrgetter

S = t.TypeVar('S', bound=pydantic.BaseModel)


class ConfigFileError(Exception):
    pass


class ConfigFile(t.Generic[S]):

    def __init__(self, file: pathlib.Path, schema: t.Type[S]) -> None:
        self.file = file
        self.schema = schema
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
            pretty_errors = pydantic.error_wrappers.display_errors(err.errors())
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
        return self.schema()

    def _create(self, force:bool=False) -> None:
        if self.file.exists() and not force:
            return
        if not self.file.exists():
            self.file.parent.mkdir(parents=True,exist_ok=True)
            self.file.touch()
        self.file.write_text(self.default_config.json())

    def _save(self) -> None:
        cfg = self.config_object.json()
        self.file.write_text(cfg)

    def _reload(self):
        self._config_object = self.raw_object

    def set(self, key:str, value:t.Any, autosave: bool=True) -> None:
        nested_config, _, attr = key.rpartition(".")        
        target = self.config_object
        if nested_config:
            try:
                nested_getter = attrgetter(nested_config)
            except AttributeError:
                raise ConfigFileError(f"There is no `{key}` config property.")
            target = nested_getter(target)
        setattr(target, attr, value)
        if autosave:
            self._save()


    def append(self, key:str, value:t.Any, autosave: bool=True) -> None:
        target_obj: t.Any = self.get(key)
        if not isinstance(target_obj, t.List):
            raise ConfigFileError(f"Target config property `{key}` is not appendable.")
        target_obj.append(value)
        if autosave:
            self._save()
    
    def remove(self, key:str, value:t.Any, autosave: bool=True) -> None:
        target_obj: t.Any = self.get(key)
        if not isinstance(target_obj, t.List):
            raise ConfigFileError(f"Target config property `{key}` is not a collection.")
        target_obj.remove(value)
        if autosave:
            self._save()

    def get(self, key:str) -> t.Any:
        value_getter = attrgetter(key)
        try:
            return value_getter(self.config_object)
        except AttributeError:
            raise ConfigFileError(f"There is no `{key}` config property.")

    def restore(self) -> None:
        self._create(force=True)

    def restore_key(self, key:str) -> None:
        value_getter = attrgetter(key)
        default_value = value_getter(self.default_config)
        self.set(key, default_value)

    def preview_full(self) -> dict:
        """ 
        Readonly full preview of the config data, any 
        change to the dict won't affect the config. 
        """
        return self.config_object.dict()
