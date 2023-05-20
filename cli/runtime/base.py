import pathlib

import typer

from cli.runtime.common import PROJECT_PACKAGE_NAME, CLI_CONFIG_FILE, CLI_DEFAULT_CONFIG

from .config import bootstrap_config
from .commands.development import get_dev_cli
from .commands.services import get_services_cli
from .config.schema import ConfigSchema


CLI = typer.Typer(
    name=f"{PROJECT_PACKAGE_NAME}.cli",
    rich_markup_mode="markdown"
)

config_cli, config_file = bootstrap_config(CLI_CONFIG_FILE, ConfigSchema, default=CLI_DEFAULT_CONFIG)
services_cli = get_services_cli(config_file.config_object)
dev_cli = get_dev_cli(config_file.config_object)

CLI.add_typer(config_cli)
CLI.add_typer(services_cli)
CLI.add_typer(dev_cli)


@CLI.command()
def shell():
    """ Interactive shell to debug the CLI envirnoment."""
    import code
    code.interact(
        banner="### LazyLab CLI Shell. ###",
        exitmsg=">>> See you later!",
        local=globals()
    )
