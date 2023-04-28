import contextvars
import pathlib
import typing as t
import rich

import typer
import pydantic

from .file import ConfigFile, ConfigFileError

config_cli = typer.Typer(name="config", no_args_is_help=True)
Config: contextvars.ContextVar[ConfigFile] =  contextvars.ContextVar("Config")


@config_cli.command("show")
def show():
    """ Show full config as JSON."""
    cfg = Config.get()
    rich.print_json(
        data=cfg.preview_full()
    )

@config_cli.command("get")
def get(property:str):
    """ Read config value.
    
    Example: config get versioning_strategy
    """
    cfg = Config.get()
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
    cfg = Config.get()
    cfg.set(property, value=value)


@config_cli.command("clear")
def clear(property:str):
    """ Clears the selected property restoring original value.
    
    Example: config clear run.silent
    """
    cfg = Config.get()
    cfg.restore_key(property)

@config_cli.command("set:append")
def append(property:str, value: str):
    """ Special set for `type:list` appends value to selected config.

    You can use `.` to access nested values.
    
    Example: config append dev.docker_files additional_docker_file.yaml
    """
    cfg = Config.get()
    cfg.append(property, value=value)


@config_cli.command("set:remove")
def remove(property:str, value: str):
    """ Special set for `type:list` removes value from selected config.
    
    You can use `.` to access nested values.
    
    Example: config remove dev.docker_files bad_file.yaml
    """
    cfg = Config.get()
    cfg.remove(property, value=value)

@config_cli.command("locate")
def locate():
    """ Open directory wth config file with system file browser."""
    cfg = Config.get()
    typer.launch(cfg.file, locate=True)


def get_config_cli(config: pathlib.Path, schema: t.Type[pydantic.BaseModel]) -> typer.Typer:
    Config.set(ConfigFile(file=config, schema=schema))
    return config_cli
