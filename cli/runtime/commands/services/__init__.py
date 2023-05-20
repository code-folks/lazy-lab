import typing as t
import typer

from contextvars import ContextVar
import rich

from cli.runtime.config.schema import ComposeConfig, ConfigSchema
from cli.runtime.common import get_docker_client, PROJECT_DIR

from .models import ComposableService


def discover_services(cfg: ComposeConfig) -> t.Iterable[ComposableService]:
    docker_client = get_docker_client(cfg=cfg)
    compose_config = docker_client.compose.config()
    for service_name, service_config in compose_config.services.items():
        yield ComposableService(
            name=service_name,
            compose_cli=docker_client.compose,
            config=service_config
        )

services_cli = typer.Typer(name="services", no_args_is_help=True)
SERVICES: ContextVar[t.List[ComposableService]] = ContextVar("SERVICES", default=[])
CFG: ContextVar[ConfigSchema] = ContextVar("CFG", default=None)

def get_versions() -> t.Dict[str, str]:
    versions = {}
    for service in SERVICES.get():
        if not service.has_sources or not service.source.has_config:
            continue
        config_key, config_value = service.source.get_config_entry("version", default="no-version", exact=False)
        origin = str(service.source.config_file.relative_to(PROJECT_DIR))
        versions[service.name] = {
            "value": config_value,
            "origin": origin,
            "config_key": config_key
        }
    return versions


@services_cli.command("all:versions")
def versions():
    """
    [:mag:] Displays local services versions
    """
    rich.print_json(data=get_versions())


def get_services_cli(config: ConfigSchema) -> typer.Typer:
    services = list(discover_services(config.docker))
    CFG.set(config)
    SERVICES.set(services)
    for service in services:
        services_cli.add_typer(service.as_command())
    return services_cli

