import json
import toml
import typing as t

from pathlib import Path

from .utils import index

CONFIG_FILES_LOADERS = {
    "package.json": json.load,
    "pyproject.toml": toml.load
}

NO_CONFIG_FILE = object()
CONFIG_VALUE = t.Union[None, int, str, bool, t.List, t.Dict]


def find_config_file(lookup_dir: Path, lookup_names: t.Iterable[str], max_depth=1, **kwargs) -> t.Optional[Path]:
    current_depth = kwargs.setdefault("current_depth", 0)
    if current_depth > max_depth:
        return None
    result = None
    for entry in lookup_dir.iterdir():
        if entry.is_file() and entry.name in lookup_names:
            return entry
        if entry.is_dir():
            result = find_config_file(entry, lookup_names, current_depth=current_depth+1)
        if result:
            return result
    return result


class Service:
    """ Abstraction to store info about available services inside project structure

    :param name: service short name.
    :param root_dir: path to the directory with the service config file.
    """
    INDEX_SEPARATOR = "."

    def __init__(self, name: str, root_dir: Path) -> None:
        self.name = name
        self.root_dir = root_dir
        self._config_file = None
        self._config_data = None

    @property
    def config_file(self) -> Path:
        if self._config_file:
            return self._config_file
        self.load_config()
        return self._config_file

    @property
    def has_config(self) -> bool:
        return self.config_file is not NO_CONFIG_FILE

    def load_config(self) -> dict:
        cfg_file = find_config_file(self.root_dir, CONFIG_FILES_LOADERS.keys())
        if cfg_file is None:
            cfg_file = NO_CONFIG_FILE
        self._config_file = cfg_file

    @property
    def config_data(self) -> t.Dict[str, CONFIG_VALUE]:
        if self._config_data is not None:
            return self._config_data
        if self.config_file is NO_CONFIG_FILE:
            self._config_data = {}
            return self._config_data
        loader = CONFIG_FILES_LOADERS.get(self.config_file.name)
        if loader is None:
            raise RuntimeError("Cannot load config data for service.")
        with self.config_file.open() as f:
            self._config_data = index(loader(f), sep=self.INDEX_SEPARATOR)
        return self._config_data

    def get_config_entry(self, key:str, default=None, exact=True) -> t.Tuple[str, CONFIG_VALUE]:
        """ Returns config entry for given key
        
        :param key: key to lookup in config data.
        :param default: default value if no entry has been found.
        :param exact: look only for exact key, when this is False, this mthod
                    will return FIRST entry that partially contains provided key

        :returns: Entry from config, which is tuple(indexed key, value) 
        """
        if exact:
            return key, self.config_data.get(key, default=default)
        for index_key, value in self.config_data.items():
            if key in index_key.lower().split(self.INDEX_SEPARATOR):
                return index_key, value
        return key, None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name={self.name}, dir={self.root_dir}>"

    __str__ = __repr__


HAS_DOCKERFILE: t.Callable[[Path], bool] = lambda d: d.joinpath("Dockerfile").exists()


def discover_services(root_dir: Path, service_check: t.Callable[[Path], bool]=HAS_DOCKERFILE) -> t.List[Service]:
    services = []
    for entry in root_dir.iterdir():
        if not entry.is_dir() or not service_check(entry):
            continue
        services.append(
            Service(name=entry.name, root_dir=entry)
        )
    return services
