from enum import Enum, auto
from typing import Iterable

import nox
from nox import Session


class Mode(Enum):
    Fix = auto()
    Check = auto()


def _type_check(session: Session) -> None:
    session.run(
        "poetry",
        "run",
        "mypy",
        # "--implicit-optional",
        # "--warn-redundant-casts",
        # "--warn-unreachable",
        # "--strict-equality",
        # "--strict",
        "--explicit-package-bases",
        "--namespace-packages",
        "--show-error-codes",
        "--pretty",
        "--show-column-numbers",
        "--show-error-context",
        "--scripts-are-modules",
        ".",
    )


def _code_format(session: Session, mode: Mode) -> None:
    isort = ["poetry", "run", "isort"]
    black = ["poetry", "run", "black"]
    isort = isort if mode == Mode.Fix else isort + ["--check"]
    black = black if mode == Mode.Fix else black + ["--check"]
    session.run(*isort, ".")
    session.run(*black, ".")


@nox.session(python=False)
def fix(session: Session) -> None:
    """Runs all automated fixes on the code base"""
    _code_format(session, Mode.Fix)


@nox.session(name="check", python=False)
def check(session: nox.Session) -> None:
    """Runs all available checks on the project"""
    _type_check(session)
    _code_format(session, Mode.Check)
