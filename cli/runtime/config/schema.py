import typing as t

from pydantic import BaseModel, fields

from .dependencies import Dependency


class ComposeConfig(BaseModel):
    compose_files: t.List[str] = []
    profiles: t.List[str] = []

class DevCommandConfig(BaseModel):
    deamon: bool = True
    use_mock: bool = True
    docker_extra: ComposeConfig = fields.Field(
        default=ComposeConfig()
    )
    dependencies: t.List[Dependency] = []

class ConfigSchema(BaseModel):
    dev: DevCommandConfig = fields.Field(default_factory=DevCommandConfig)
    docker: ComposeConfig = fields.Field(default_factory=ComposeConfig)
