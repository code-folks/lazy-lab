import pathlib
import typing as t
from python_on_whales import DockerClient

from .config_schema import ComposeConfig
from .utils import merge

project_root = pathlib.Path(__file__).parent.parent


def get_docker_client(cfg: t.Optional[ComposeConfig]=None) -> DockerClient:
    if cfg is None:
        return DockerClient(compose_project_directory=project_root)
    return DockerClient(
        compose_files=cfg.compose_files, compose_profiles=cfg.profiles, compose_project_directory=project_root
    )


def merge_compose_configs(*configs: ComposeConfig) -> ComposeConfig:
    cfg_dicts = [ c.dict() for c in configs ]
    outer = cfg_dicts.pop()
    for d in cfg_dicts:
        outer = merge(outer, d)
    return ComposeConfig.parse_obj(outer)
