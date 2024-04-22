__all__ = [
    "prt",
    "inp",
    "clear_terminal",
]

import os
from typing import Any, Union
from typing_extensions import LiteralString

from src.logger import *

AnyOrStr = Union[Any, str]


def prt(*s: AnyOrStr, i: AnyOrStr = "") -> None:
    """
    The function `prt` logs a function call with the provided arguments and prints the given strings
    with an optional string as a separator.

    @param *s The `*s` parameter in the `prt` function is a variable number of string arguments
    that will be printed.
    @param i The `i` parameter in the `prt` function is an optional string argument used as a separator
    in the printed output.
    """
    logger_specials.was_called(__name__, prt.__name__)
    return print(*s, i)


def inp(s: LiteralString = "") -> str:
    """
    The function `inp` logs a function call with the provided argument and prompts the user for input,
    displaying the provided string as a prompt.

    @param s The `s` parameter in the `inp` function is an optional string argument used as a prompt
    for the user input.

    @return str The function `inp` returns the user input as a string.
    """
    logger_specials.was_called(__name__, inp.__name__)
    return input(f"{s}\n> ")


def clear_terminal() -> int:
    """
    The function `clear_terminal` clears the terminal screen by calling the appropriate system command
    based on the operating system. If the operating system is Windows, it executes the command "cls";
    otherwise, it executes the command "clear".

    @return The function `clear_terminal` returns an integer representing the exit status of the system
    command execution.
    """
    logger_specials.was_called(__name__, clear_terminal.__name__)
    return os.system("cls" if os.name == "nt" else "clear")
