import re
import typing as t
import secrets
import pathlib

import rich
import typer

from rich.table import Table
from pydantic import BaseModel, fields

dependency_prompt: str = """
[indian_red1]Resolving `{name}` dependency.
Go to: [dark_olive_green1][link={help_url}]{help_url}[/link][/dark_olive_green1] to get more information.
"""


class Modificator(BaseModel):
    generator: t.Optional[t.Callable] = fields.Field(default=None)
    auto: bool = fields.Field(default=False)
    prompt_options: t.Optional[t.Dict[str, t.Any]] = fields.Field(default_factory=dict)


slots_matcher = re.compile(r"{{(?P<template_slot>.*)}}")
modificators: t.Dict[str, Modificator] = {
    "int": Modificator(prompt_options={"type": int}),
    "float": Modificator(prompt_options={"type": float}),
    "autotoken": Modificator(generator=secrets.token_urlsafe, auto=True),
    "defaultsecret": Modificator(generator=secrets.token_urlsafe, prompt_options={"hide_input": True}),
    "secret": Modificator(prompt_options={"hide_input": True}),
}


class TemplateSlot(BaseModel):
    separator: t.ClassVar[str] = ":"
    token: str = ...

    _name: str = fields.PrivateAttr(default=None)
    _modificators: t.List[Modificator] = fields.PrivateAttr(default=None)

    @property
    def name(self):
        if self._name is not None:
            return self._name
        if TemplateSlot.separator not in self.token:
            self._name = self.token
            return self.token
        name, *_ = self.token.split(TemplateSlot.separator)
        self._name = name
        return name

    @property
    def modificators(self) -> t.List[Modificator]:
        if self._modificators is not None:
            return self._modificators
        mods = []
        self._modificators = mods
        if TemplateSlot.separator not in self.token:
            return mods
        _, *mods_array = self.token.split(TemplateSlot.separator)
        for mod in mods_array:
            modificator = modificators.get(mod, None)
            if modificator is None:
                continue
            mods.append(modificator)
        return mods

    @property
    def prompt_options(self):
        options = {}
        for mod in self.modificators:
            options.update(mod.prompt_options)
        return options

    def get_default(self) -> t.Tuple[bool, t.Any]:
        for mod in self.modificators:
            if mod.generator:
                return mod.auto, mod.generator()
        return None

    def prompt_for_value(self) -> t.Any:
        auto, default = self.get_default()
        if auto:
            return default
        try:
            value: str = typer.prompt(
                text=f"Set `{self.name}`",
                default=default,
                **self.prompt_options
            )
        except typer.Abort as err:
            return None
        return value


class Dependency(BaseModel):
    name: str = ...
    target: pathlib.Path = ...
    template: pathlib.Path = ...
    # If the dependency is not found we will
    # provide help_url so the user can provide it
    help_url: t.Optional[str] = None

    _template_content: str = fields.PrivateAttr(default="")

    def fullfiled(self) -> bool:
        return self.target.exists()

    def create_target(self):
        self.target.parent.mkdir(parents=True, exist_ok=True)
        self.target.touch()

    def write_content(self, content: str):
        self.target.write_text(content)

    def fill_slots(self, slots_resolutions: t.Dict[str, str]):
        for token, slot_value in slots_resolutions.items():
            self._template_content = self._template_content.replace("{{" + token + "}}", slot_value)
        self.write_content(self._template_content)

    def resolve(self) -> bool:
        rich.print(dependency_prompt.format(name=self.name, help_url=self.help_url))
        self.create_target()
        slots = self.gather_slots()
        slots_resolutions = {}
        for slot in slots:
            resolved_value = slot.prompt_for_value()
            slots_resolutions[slot.token] = str(resolved_value)
        self.fill_slots(slots_resolutions=slots_resolutions)
        return False

    def gather_slots(self) -> t.List[TemplateSlot]:
        """Gathers all missing slots in dependency template."""
        self._template_content = self.template.read_text()
        slot_tokens = set(slots_matcher.findall(self._template_content))
        return [ TemplateSlot(token=st) for st in slot_tokens ]


def check_dependencies(
    dependencies: t.Iterable[Dependency],
) -> t.Iterable[t.Tuple[Dependency, bool]]:
    for dependency in dependencies:
        yield (dependency, dependency.fullfiled())


def resolve_dependencies(
    dependencies: t.Iterable[Dependency],
    show_summary: bool = True,
    table_name: t.Optional[str] = None,
) -> t.List[Dependency]:
    """Checks if given dependnecies are fullfiled.
    This function will try to resolve missing dependencies by asking user for input.
    Returns list of unresolved dependnecies if some cannot be resolved.

    :param summary_table: title for a summary table. If not provided, no table will be displayed.
    """
    table = Table("dependency", "location", "status", title=table_name)
    unfullfiled: t.List[Dependency] = []
    for dep, fullfiled in check_dependencies(dependencies=dependencies):
        if not fullfiled:
            unfullfiled.append(dep)
        status = "💚" if fullfiled else "❌"
        table.add_row(dep.name, str(dep.target), status)
    if show_summary:
        rich.print(table)
    if not unfullfiled:
        return []
    if not typer.confirm("Do you want to resolve them now?", default=False):
        return unfullfiled
    unresolved = []
    for dep in unfullfiled:
        resolved = dep.resolve()
        if not resolved:
            unresolved.append(dep)
    return unresolved
