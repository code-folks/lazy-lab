import pathlib
import typing as t

from pydantic import BaseModel, fields


class ComposeConfig(BaseModel):
    compose_files: t.List[str] = ["docker-compose.yaml", ]
    profiles: t.List[str] = ["essential",]

class DevCommandConfig(BaseModel):
    deamon: bool = True
    docker_extra: ComposeConfig = fields.Field(
        default=ComposeConfig(compose_files=["@compose/dev.yaml",], profiles=[])
    )

class ConfigSchema(BaseModel):
    dev: DevCommandConfig = fields.Field(default_factory=DevCommandConfig)
    docker: ComposeConfig = fields.Field(default_factory=ComposeConfig)
    project_root: str = str(pathlib.Path(__file__).parent.parent)
