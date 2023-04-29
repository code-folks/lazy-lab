import typing as t

from python_on_whales import DockerClient

from .config_schema import ComposeConfig


def get_docker_client(cfg: t.Optional[ComposeConfig]=None) -> DockerClient:
    if cfg is None:
        return DockerClient()
    return DockerClient(compose_files=cfg.compose_files, compose_profiles=cfg.profiles)
