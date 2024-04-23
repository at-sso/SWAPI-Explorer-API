__all__ = ["lang", "lang_values"]

import argparse
from argparse import (
    Namespace,
)
from typing import Callable, Dict

from src.file_handler import *
from src.const import *


def __lang_file_handler(filename: str = "", force_ex: bool = False) -> str:
    if force_ex:
        raise ValueError(
            "Language setting is not specified or is set to 'null'."
            "Please provide a valid language setting."
            f"Global lang: {lang}"
        )
    return load_file(f"{LANG_PATH}/{filename}.txt")["content"]


def __parse_args() -> Namespace:
    parser = argparse.ArgumentParser(
        prog="SWAPI-Explorer-API/main.py",
    )

    parser.add_argument(
        "-EN",
        default=False,
        action="store_true",
        help="(BOOLEAN) - Set the API output responses to English. (Default is False)",
    )

    parser.add_argument(
        "-ES",
        default=False,
        action="store_true",
        help="(BOOLEAN) - Establece las respuestas de salida de la API en español. "
        "(El valor predeterminado es False)",
    )

    return parser.parse_args()


__args: Namespace = __parse_args()

lang: str = "null"
lang_values: Dict[str, Callable[[], str]] = {
    "en": lambda: __lang_file_handler("en"),
    "es": lambda: __lang_file_handler("es"),
    "null": lambda: __lang_file_handler(force_ex=True),
}

# If both values weren't set, the 'EN' mode is loaded by default.
if not (__args.EN or __args.ES):
    __args.EN = True

# Set lang as 'EN' if 'EN' is True, else 'ES'
lang = "en" if __args.EN else "es"
