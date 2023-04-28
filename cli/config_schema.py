import typing as t

from pydantic import BaseModel, fields


class DevCommandConfig(BaseModel):
    docker_files: t.List[str] = [ "docker-compose.yaml", "@compose/dev.yaml",]
    profile: str = "essential"
    deamon: bool = True


class ConfigSchema(BaseModel):
    dev: DevCommandConfig = fields.Field(default_factory=DevCommandConfig)
