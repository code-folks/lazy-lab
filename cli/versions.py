import typing as t

from rich import print, print_json

from .base import CLI, PROJECT_PACKAGE_NAME, SERVICES, PROJECT_DIR


def get_versions() -> t.Dict[str, str]:
    versions = {}
    for service in SERVICES:
        config_key, config_value = service.get_config_entry("version", default="no-version", exact=False)
        if not service.has_config:
            continue
        origin = str(service.config_file.relative_to(PROJECT_DIR))
        versions[service.name] = {
            "value": config_value,
            "origin": origin,
            "config_key": config_key
        }
    return versions


@CLI.command("versions")
def show_versions():
    """
    [:mag:] Displays current Services **versions**
    """
    print(f"\n[magenta underline]{PROJECT_PACKAGE_NAME} Services Versions[/magenta underline]:\n")
    print_json(data=get_versions())

@CLI.command()
def dupa():
    pass