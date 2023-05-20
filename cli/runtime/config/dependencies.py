import typing as t
import pathlib

import rich
import typer

from rich.table import Table
from pydantic import BaseModel

dependency_prompt: str = """
[indian_red1]It looks like you are missing `{name}` dependency.
Go to: [dark_olive_green1][link={help_url}]{help_url}[/link][/dark_olive_green1]
to get more information.
"""


class Dependency(BaseModel):

    name: str = ...
    target: pathlib.Path = ...
    # If the dependency is not found we will
    # provide help_url so the user can provide it
    secret: bool = False
    help_url: t.Optional[str] = None

    def fullfiled(self) -> bool:
        return self.target.exists()

    def prompt(self) -> bool:
        rich.print(
            dependency_prompt.format(name=self.name, help_url=self.help_url)
        )
        try:
            value: str = typer.prompt(
                text=f"Set `{self.name}`", default=None, hide_input=self.secret)
        except typer.Abort as err:
            return False
        if not value.strip():
            return False
        self.target.parent.mkdir(parents=True, exist_ok=True)
        self.target.touch()
        self.target.write_text(value)
        rich.print(f"Dependency saved at: [steel_blue1]{self.target}")
        return True


def check_dependencies(dependencies: t.Iterable[Dependency]) -> t.Iterable[t.Tuple[Dependency, bool]]:
    for dependency in dependencies:
        yield (dependency, dependency.fullfiled())


def resolve_dependencies(
    dependencies: t.Iterable[Dependency],
    show_summary:bool=True, 
    table_name: t.Optional[str] = None,
) -> t.List[Dependency]:
    """ Checks if given dependnecies are fullfiled. 
    This function will try to resolve missing dependencies by asking user for input. 
    Returns list of unresolved dependnecies if some cannot be resolved.

    :param summary_table: title for a summary table. If not provided, no table will be displayed.
    """
    table = Table('dependency', 'location', 'is secret?', 'status', title=table_name)
    unfullfiled: t.List[Dependency] = []
    for dep, fullfiled in check_dependencies(dependencies=dependencies):
        if not fullfiled:
            unfullfiled.append(dep)
        status = "💚" if fullfiled else "❌"
        is_secret = "yes" if dep.secret else "no"
        table.add_row(dep.name, str(dep.target), is_secret, status)
    if show_summary:
        rich.print(table)
    if not unfullfiled:
        return []
    if not typer.confirm("Do you want to resolve them now?", default=False):
        return unfullfiled
    unresolved = []
    for dep in unfullfiled:
        resolved = dep.prompt()
        if not resolved:
            unresolved.append(dep)
    return unresolved
