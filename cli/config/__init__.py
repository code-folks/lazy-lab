import contextvars
import pathlib
import typing as t

from contextlib import contextmanager

import rich
import typer
import pydantic

from .file import ConfigFile, ConfigFileError

config_cli = typer.Typer(name="config", no_args_is_help=True)
Config: contextvars.ContextVar[ConfigFile] =  contextvars.ContextVar("Config")


@contextmanager
def errorles_config(error_emoji:str=":no_entry:", succes_emoji: t.Optional[str] = None):
    cfg = Config.get()
    try:
        yield cfg
        if not succes_emoji:
            return
        rich.print(succes_emoji)
    except ConfigFileError as err:
        rich.print(f"{error_emoji} {err}")


@config_cli.command("show")
def show():
    """ Show full config as JSON."""
    with errorles_config() as cfg:
        rich.print_json(
            data=cfg.preview_full()
        )

@config_cli.command("get")
def get(property:str):
    """ Read config value.
    
    Example: config get versioning_strategy
    """
    with errorles_config() as cfg:
        rich.print_json(
            data={property: cfg.get(property)}
        )

@config_cli.command("set")
def set(property:str, value: str):
    """ Sets config value.
    
    You can use `.` to access nested values.
    When given property is an collection we recomend using `append` command.

    Example: config set dev.profile my-profile 
    """
    with errorles_config(succes_emoji=":thumbsup:") as cfg:
        cfg.set(property, value=value)


@config_cli.command("clear")
def clear(property:str):
    """ Clears the selected property restoring original value.
    
    Example: config clear run.silent
    """
    with errorles_config(succes_emoji=":thumbsup:") as cfg:
        cfg.restore_key(property)


@config_cli.command("clear:all")
def clear():
    """ Clears the selected property restoring original value.
    
    Example: config clear run.silent
    """
    with errorles_config(succes_emoji=":thumbsup:") as cfg:
        typer.confirm("Are you sure? This will 💥 whole config❗:", abort=True)
        cfg.restore()


@config_cli.command("set:append")
def append(property:str, value: str):
    """ Special set for `type:list` appends value to selected config.

    You can use `.` to access nested values.
    
    Example: config append dev.docker_files additional_docker_file.yaml
    """
    with errorles_config(succes_emoji=":thumbsup:") as cfg:
        cfg.append(property, value=value)


@config_cli.command("set:remove")
def remove(property:str, value: str):
    """ Special set for `type:list` removes value from selected config.
    
    You can use `.` to access nested values.
    
    Example: config remove dev.docker_files bad_file.yaml
    """
    with errorles_config(succes_emoji=":thumbsup:") as cfg:
        cfg.remove(property, value=value)

@config_cli.command("locate")
def locate():
    """ Open directory wth config file with system file browser."""
    with errorles_config(succes_emoji=":thumbsup:") as cfg:
        typer.launch(cfg.file.as_uri(), locate=True)


C = t.TypeVar("C", bound=pydantic.BaseModel)

def bootstrap_config(config: pathlib.Path, schema: t.Type[C]) -> t.Tuple[typer.Typer, ConfigFile[C]]:
    Config.set(ConfigFile(file=config, schema=schema))
    return config_cli, Config.get()
