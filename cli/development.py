from contextvars import ContextVar
from contextlib import contextmanager

import typer
import rich

from python_on_whales.exceptions import DockerException

from .config_schema import ConfigSchema
from .docker import  get_docker_client, merge_compose_configs


dev_cli = typer.Typer(name="dev", no_args_is_help=True)
DEV_CFG: ContextVar[ConfigSchema] = ContextVar("CFG", default=None)
GATEWAY_LINK = "http://localhost:8080/auth/login"
MOCK_GATEWAY_LINK = "http://mock.localhost:8080/auth/login"

@contextmanager
def dev_client():
    cfg = DEV_CFG.get()
    merged_config = merge_compose_configs(cfg.docker, cfg.dev.docker_extra)
    docker_client = get_docker_client(cfg=merged_config)
    try:
        yield docker_client
    except DockerException as err:
        rich.print(f":whale::dash: Docker says:\n {err}")
        typer.Exit(1)


@dev_cli.command("run")
@dev_cli.command("start")
def run(d: bool = True, all: bool = False, build: bool=False, browser:bool=True):
    """ Starts the development envirnoment using the configured deveopment files. """
    dev_cfg = DEV_CFG.get().dev
    with dev_client() as docker_client:
        console = rich.console.Console(soft_wrap=True)
        with console.status("[plum1] Starting [plum2]development [plum3]envirnoment[plum4]... :rocket:", spinner="moon"):
            docker_client.compose.up(detach=d, abort_on_container_exit=all, wait=d, build=build, quiet=True)
    console.print("[cyan3] :spouting_whale: Project started...")
    link_to_open = MOCK_GATEWAY_LINK if dev_cfg.use_mock else GATEWAY_LINK
    if browser:
        typer.launch(link_to_open)


@dev_cli.command("stop")
def stop():
    """ Stops all the dev containers."""
    with dev_client() as docker_client:
        console = rich.console.Console(soft_wrap=True)
        with console.status("Shuting down... :clap:", spinner="arc"):
            docker_client.compose.down(quiet=True)
    console.print("[cyan3] :hand: Done...")


def get_dev_cli(config: ConfigSchema) -> typer.Typer:
    DEV_CFG.set(config)
    return dev_cli
