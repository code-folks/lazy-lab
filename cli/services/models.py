import json
import toml
import inspect

import typing as t
from contextlib import contextmanager
from pathlib import Path

import typer
import rich

from python_on_whales.components.compose.cli_wrapper import ComposeCLI
from python_on_whales.components.compose.models import ComposeConfigService
from python_on_whales.exceptions import DockerException

from ..utils import index

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


class ServiceSource:
    """ Abstraction to store info about service source in project structure

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


NO_SERVICE_SOURCE = object()

@contextmanager
def clear_compose():
    try:
        yield
    except DockerException as err:
        rich.print(
            "🔺 There was a problem with Docker command, check line ABOVE more details.\n"
            f"Command: `{err.docker_command}`"
        )


def expose_to_cli(func: t.Callable):
    func._exposed = True
    return func

def is_exposed(method) -> bool:
    return ( 
        inspect.ismethod(method) and 
        hasattr(method.__func__, '_exposed') and 
        method.__func__._exposed
    )

class ComposableService:

    def __init__(self, name: str, config: ComposeConfigService, compose_cli: ComposeCLI) -> None:
        self.name = name
        self.config = config
        self.compose = compose_cli
        self._source = None

    @property
    def source(self) -> ServiceSource:
        if self._source is None:
            build_config = self.config.build
            if build_config is None or build_config.context is None:
                self._source = NO_SERVICE_SOURCE
                return self._source
            self._source = ServiceSource(self.name, root_dir=build_config.context)
        return self._source

    @property
    def has_sources(self) -> bool:
        return self.source is not NO_SERVICE_SOURCE

    @property
    def compose_id(self) -> t.List[str]:
        return [self.name,]


    @expose_to_cli
    def build(self, quiet: bool=True):
        """ Builds service 

        EQUIVALENT OF => `docker compose build *service-name*`."""
        self.compose.build(self.compose_id, quiet=quiet)

    @expose_to_cli
    def run(self, command: str):
        """ Runs command inside service container 

        EQUIVALENT OF => `docker compose run *service-name* COMMAND`."""
        with clear_compose():
            self.compose.run(self.name, command=[command])

    @expose_to_cli
    def shell(self):
        """ Runs command inside service container 

        EQUIVALENT OF => `docker compose exec *service-name* bash`."""
        try_commands = ["bash", "sh"]
        with clear_compose():
            last_exception = None
            for command in try_commands:
                try:
                    self.compose.execute(self.name, command=[command])
                except DockerException as err:
                    last_exception = err
                    continue
            if last_exception is not None:
                raise last_exception

    @expose_to_cli
    def up(self, force_recreate:bool=False, detach:bool=True):
        """ Starts the service container 

        EQUIVALENT OF => `docker compose up *service-name*`."""
        with clear_compose():
            self.compose.up(self.compose_id, force_recreate=force_recreate, detach=detach)

    @expose_to_cli
    def logs(self, timestamps:bool=False, follow:bool=False, tail:str = "all", short_prefix:bool=True):
        """ Stops the service container 

        EQUIVALENT OF => `docker compose logs *service-name*`."""
        template = "{prefix} | {data}" if short_prefix else "{data}"
        with clear_compose():
            logs_stream = self.compose.logs(
                self.compose_id, timestamps=timestamps, follow=follow, tail=tail, no_log_prefix=short_prefix, stream=True
            )
            for source, data in logs_stream:
                rich.print(template.format(data=data.decode('utf-8'), prefix=f"{self.name}"), end="")

    @expose_to_cli
    def down(self):
        """ Stops the service container 

        EQUIVALENT OF => `docker compose stop *service-name*`."""
        with clear_compose():
            self.compose.stop(self.compose_id)

    @expose_to_cli
    def kill(self):
        """ Kills the service container 

        EQUIVALENT OF => `docker compose kill *service-name*`."""
        with clear_compose():
            self.compose.kill(self.compose_id)


    def _get_exposed_methods(self) -> t.Iterable[t.Callable]:
        return inspect.getmembers(self, is_exposed)

    def as_command(self) -> typer.Typer:
        service_cli = typer.Typer(name=self.name.lower())
        exposed_methods = self._get_exposed_methods()
        for method_name, method in exposed_methods:
            help_doc = inspect.getdoc(method).replace("*service-name*", self.name.lower())
            register_command = service_cli.command(name=method_name, help=help_doc)
            register_command(method)
        return service_cli
