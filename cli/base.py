import pathlib

import typer
import pydantic

from .services import discover_services

PROJECT_PACKAGE_NAME="lazy-lab"
PROJECT_DIR = pathlib.Path(__file__).parent.parent

SERVICES = discover_services(PROJECT_DIR / "services")
CLI = typer.Typer(
    name=f"{PROJECT_PACKAGE_NAME}.cli",
    rich_markup_mode="markdown"
)

CLI_CONFIG_DIR = typer.get_app_dir(PROJECT_PACKAGE_NAME)
CLI_CONFIG_DIR_PATH: pathlib.Path = pathlib.Path(CLI_CONFIG_DIR) / "config.json"

class CLIConfig(pydantic.BaseModel):
    pass

config_cli = typer.Typer()















CLI.add_typer(config_cli)
