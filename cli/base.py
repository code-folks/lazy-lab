import pathlib

import typer

# from .services import discover_services
from .config import bootstrap_config
from .services import get_services_cli
from .config_schema import ConfigSchema

PROJECT_PACKAGE_NAME="lazy-lab"
PROJECT_DIR = pathlib.Path(__file__).parent.parent

SERVICES = []
# discover_services(PROJECT_DIR / "services")
CLI = typer.Typer(
    name=f"{PROJECT_PACKAGE_NAME}.cli",
    rich_markup_mode="markdown"
)

CLI_CONFIG_DIR = typer.get_app_dir(PROJECT_PACKAGE_NAME)
CLI_CONFIG_FILE: pathlib.Path = pathlib.Path(CLI_CONFIG_DIR) / "config.json"


config_cli, config_file = bootstrap_config(CLI_CONFIG_FILE, ConfigSchema)
services_cli = get_services_cli(config_file.config_object)

CLI.add_typer(config_cli)
CLI.add_typer(services_cli)
