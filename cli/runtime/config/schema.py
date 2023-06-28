import typing as t

from pydantic import BaseModel, fields

from .dependencies import Dependency


class ComposeConfig(BaseModel):
    compose_files: t.List[str] = []
    profiles: t.List[str] = []


class OrchestrationStep(BaseModel):
    name: str = ...
    env_file: t.Optional[str] = fields.Field(default=None)
    services: t.List[str] = fields.Field(default_factory=list)
    dependencies: t.List[Dependency] = fields.Field(default_factory=list)
    ready_url: t.Optional[str] = fields.Field(default=None)

class DevCommandConfig(BaseModel):
    deamon: bool = True
    use_mock: bool = True
    docker: ComposeConfig = fields.Field(
        default=ComposeConfig()
    )
    start_steps: t.List[OrchestrationStep] = fields.Field(default_factory=list)
    stop_steps: t.List[OrchestrationStep] = fields.Field(default_factory=list)

class ConfigSchema(BaseModel):
    dev: DevCommandConfig = fields.Field(default_factory=DevCommandConfig)
    docker: ComposeConfig = fields.Field(default_factory=ComposeConfig)
    dependencies: t.List[Dependency] = fields.Field(default_factory=list)
