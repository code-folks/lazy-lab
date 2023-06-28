import pathlib
import typing as t

from python_on_whales import DockerClient

from .config.schema import ComposeConfig
from .utils import merge

PROJECT_PACKAGE_NAME = "lazy-lab"

CLI_DIR = pathlib.Path(__file__).parent.parent
PROJECT_DIR = CLI_DIR.parent
CLI_CONFIG_FILE: pathlib.Path = PROJECT_DIR / "config.local.json"
CLI_DEFAULT_CONFIG: pathlib.Path = CLI_DIR / "config.default.json"


def get_docker_client(cfg: t.Optional[ComposeConfig]=None, env_file: t.Optional[str]=None) -> DockerClient:
    if cfg is None:
        return DockerClient(compose_project_directory=PROJECT_DIR)
    return DockerClient(
        compose_files=cfg.compose_files,
        compose_profiles=cfg.profiles,
        compose_project_directory=PROJECT_DIR,
        compose_env_file=env_file
    )


def merge_compose_configs(*configs: ComposeConfig) -> ComposeConfig:
    cfg_dicts = [ c.dict() for c in configs ]
    outer = cfg_dicts.pop()
    for d in cfg_dicts:
        outer = merge(outer, d)
    return ComposeConfig.parse_obj(outer)
