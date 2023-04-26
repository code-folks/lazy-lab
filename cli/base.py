import typer
import pathlib

from .services import Service, discover_services

PROJECT_PACKAGE_NAME="LazyLab"
PROJECT_DIR = pathlib.Path(__file__).parent.parent

SERVICES = discover_services(PROJECT_DIR / "services")

CLI = typer.Typer(
    name=f"{PROJECT_PACKAGE_NAME}.cli",
    rich_markup_mode="markdown"
)
