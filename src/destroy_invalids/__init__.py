__all__ = ["destroy_invalids"]

import re
from typing import List, Any, Tuple, Callable
from typing_extensions import LiteralString

from src.logger import *
from src.var import *


def _was_called_from_specific(
    func_name: Callable[..., Any],
    func_args: Tuple[Any, ...] | str,
    init: str = "<Unkown>",
) -> None:
    """
    The function `_was_called_from_specific` logs the invocation of a function along with its arguments.

    @param func_name The `func_name` parameter is a callable representing the name of the function being called.
    @param func_args The `func_args` parameter is a tuple containing the arguments passed to the function.
    @param init The `init` parameter is a string representing the context or initialization point where the function was called.
    """
    logger_specials.was_called(func_name=func_name.__name__, key="debug", init=init)
    logger_specials.from_specific(func=init, func_args=func_args)


class __DestroyInvalids:
    def alphanumeric_only(
        self,
        data: Tuple[str, ...] | str,
        init: Callable[..., Any],
        extras: LiteralString = "",
    ) -> List[str]:
        """
        The function `alphanumeric_only` filters alphanumeric characters from input strings or a single string,
        replacing spaces with underscores. It utilizes regex to find valid characters, handles logging and returns
        a list of filtered strings.

        @param data The `data` parameter represents input strings or a single string. If it's a single string,
        it's converted to a tuple for uniform processing.
        @param init The `init` parameter represents a callable function. Logging is performed with this function.
        @param extras The `extras` parameter contains additional characters to consider valid apart from
        alphanumeric characters.

        @return The function returns a list of filtered strings, where non-alphanumeric characters are removed
        and spaces are replaced by underscores. If an input string is empty, an empty string is returned in
        the list.
        """
        _was_called_from_specific(self.alphanumeric_only, data, init.__name__)

        # Define a regex pattern to match symbols
        valid_chars: LiteralString = rf"[a-zA-Z0-9_{extras}]"

        return_values: List[str] = list()

        # If `data` is a single string, convert it to a tuple for uniform processing
        if isinstance(data, str):
            data = (data,)

        # Iterate over each input string.
        for string in data:
            string = string.replace(" ", "_")
            # Use regex to find valid characters in the input string.
            valid_characters: List[Any] = re.findall(
                valid_chars, string, flags=re.IGNORECASE
            )
            # Join the valid characters to form the filtered string.
            filtered_string: str = "".join([match[0] for match in valid_characters])
            # Append the given parameter with the filtered string.
            return_values.append(filtered_string)
            logger_specials.value_was_set(
                value_name=string,
                value=filtered_string,
                callable=init,
            )
        return return_values

    @staticmethod
    def flags_only(input_list: List[str]) -> None:
        """
        The method `flags_only` removes flag strings from a list of strings.

        @param input_list The `input_list` parameter in `flags_only` is a list of strings containing flags
        and non-flag strings.
        """
        input_list[:] = [
            s for s in input_list if not s.startswith("/") and not s.startswith(".")
        ]

    @staticmethod
    def non_flags_only(input_list: List[str]) -> None:
        """
        The method `non_flags_only` removes non-flag strings from a list of strings.

        @param input_list The `input_list` parameter in `non_flags_only` is a list of strings containing
        flags and non-flag strings.
        """
        input_list[:] = [
            s for s in input_list if s and s.startswith("/") or s.startswith(".")
        ]

    def numeric_only(
        self, input_string: str, instance: Callable[[str], int | float]
    ) -> int | float:
        """
        The function `numeric_only` sanitizes an input string to contain only numeric characters (digits and
        decimal point), using a regular expression. If the resulting string is empty, it returns 0. Otherwise,
        it calls the provided instance function with the sanitized input string.

        @param input_string The `input_string` parameter in the `numeric_only` function is a string that
        contains alphanumeric characters. This parameter is sanitized to remove any non-numeric characters
        before processing.
        @param instance The `instance` parameter in the `numeric_only` function is a callable object that
        accepts a string argument and returns either an integer or a float value.

        @return The function `numeric_only` returns either an integer or a float value, depending on the
        result of calling the provided instance function with the sanitized input string.
        """
        logger_specials.was_called(__name__, self.numeric_only.__name__)
        input_string = re.sub(r"[^0-9.]", "", input_string)
        if input_string == "":
            return var.limit
        try:
            return instance(input_string)
        except ValueError:
            logger_specials.unexpected_error("handling", input_string)
            return var.limit

    def anything(self, value: str, remove: str) -> str:
        """
        The function `anything` takes a string `value` and a string `remove`, and modifies `value` by removing all
        characters that are not present in the `remove` string. If `value` becomes an empty string after the
        modification, a warning message is logged and the string "NULL" is returned.

        @param value The `value` parameter in the `anything` method is a string that will be modified by
        removing all characters that are not present in the `remove` parameter.
        @param remove The `remove` parameter in the `anything` method is a string containing characters that are
        allowed to remain in the `value` string after modification.

        @return The function `anything` returns the modified `value` string. If the modified `value` string
        becomes empty, the function logs a warning message and returns the string "NULL".
        """
        _was_called_from_specific(self.anything, value)
        re_format: str = rf"[^{remove}]"
        value = re.sub(re_format, "", value)
        if value == "":
            logger.warning(
                f"The returned `value` is empty: '{value}'. "
                f"This value was tried to be modified using: '{re_format}'."
            )
            return "NULL"
        return value


destroy_invalids = __DestroyInvalids()
"The `DestroyInvalids` class provides methods for sanitizing input strings."
