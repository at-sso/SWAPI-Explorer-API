__all__ = ["lang"]

import argparse
from argparse import (
    Namespace,
)

lang: str = "null"


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

# If both values weren't set, the 'EN' mode is loaded by default.
if not (__args.EN or __args.ES):
    __args.EN = True

# Set lang as 'EN' if 'EN' is True, else 'ES'
lang = "en" if __args.EN else "es"
