__all__ = ["var"]

import ctypes
import random
import time
import sys

from src.const import SHARED_FILE


def _random64() -> float:
    """
    The function `_random64` generates a random number using the shared library `random64`. If an
    exception occurs during the loading of the library, the function seeds the random number generator
    with the current time and generates a random number within a specified range.

    @return The function `_random64` returns a floating-point number, either obtained from the shared
    library or generated locally using Python's built-in modules.
    """
    try:
        # Load the shared library.
        random64_lib = ctypes.CDLL(SHARED_FILE)
        # Define the return type to float.
        random64_lib.random64.restype = ctypes.c_float
        return random64_lib.random64()
    except:
        MAX_UNICODE: int = sys.maxunicode
        # Seed the random number generator with current time.
        random.seed(time.time() + MAX_UNICODE / 0.9 - (MAX_UNICODE / 20))
        # Generate a random number between 0 and INT32_MAX (sys.maxunicode).
        random_number: int = random.randint(0, MAX_UNICODE)
        # Adjust the range to the desired min-max values.
        range_value: float = MAX_UNICODE - (MAX_UNICODE / 2) + MAX_UNICODE / 2
        # Scale the random number to fit within the range.
        scaled_number: float = random_number % range_value
        # Return the random number within the scaled_number range.
        return scaled_number


class __Var:
    extra_message: str = "Good looking!"
    limit: float = _random64()


var = __Var
