import requests
from typing import List, Any, Type

from .file_handler import *
from .functions import *
from .lang_helper import *
from .logger import *
from .const import *
from .var import *

SWAPI = "https://swapi.dev/api"
ResponseType = Type[requests.Response]


def __get_request(route: str, verify: bool = False) -> ResponseType:
    """
    The function `__get_request` performs an HTTP GET request to the specified `route`, with an optional
    `verify` parameter to enable/disable SSL certificate verification.

    @param route The `route` parameter is a string specifying the URL to which the GET request will be
    sent.
    @param verify The `verify` parameter is a boolean flag that determines whether SSL certificate
    verification should be performed. It defaults to `False` if not explicitly specified.

    @return The function `__get_request` returns a `Response` object containing the server's response
    to the HTTP GET request.
    """
    return requests.get(route, verify=verify)


def main() -> int:
    "Main function"
    logger.info("Main function started.")
    logger_specials.was_called(__name__, main.__name__)

    # Initialize the global language string variable based on the current language setting.
    if lang == "null":
        raise ValueError("")

    if lang == "en":
        var.global_str = load_file(f"{LANG_PATH}/en.txt")["content"]
    else:
        var.global_str = load_file(f"{LANG_PATH}/es.txt")["content"]

    logger_specials.value_was_set("var.global_str", f"\n{var.global_str}\n")

    # Perform a GET request to fetch the list of planets.
    api_planet_response: ResponseType = __get_request(f"{SWAPI}/planets")
    api_planet_data: Any = api_planet_response.json()
    api_starships_response: ResponseType = __get_request(f"{SWAPI}/starships")
    api_starships_data: Any = api_starships_response.json()

    # Initialize a list to store the names of films with arid planets.
    arid_films: List[Any] = []

    # Iterate over each planet and check if its climate is arid.
    for planet in api_planet_data["results"]:
        if "arid" in planet["climate"].lower():
            # If the climate is arid, gather information about the films it appears in.
            for film_url in planet["films"]:
                film_response: ResponseType = __get_request(film_url)
                film_data: Any = film_response.json()
                # Store the film title if it's not already in the list.
                if film_data["title"] not in arid_films:
                    arid_films.append(film_data["title"])

    arid_films_values: int = len(arid_films)
    # log the number of films with arid planets.
    logger.info(arid_films_values)

    # Initialize a variable to store the count of Wookiees.
    wookie_count: int = 0

    # Iterate over each species and check if it's Wookiee.
    for species in api_planet_data["results"]:
        if species["name"] == "Wookiee":
            # Gather information about characters belonging to the Wookiee species.
            for character_url in species["people"]:
                character_response: ResponseType = __get_request(character_url)
                character_data: Any = character_response.json()
                # Increment the Wookiee count.
                wookie_count += 1

    # log the number of Wookiees across the saga.
    logger.info(wookie_count)

    # Initialize variables to store the name and size of the smallest starship.
    smallest_starship_name: Any = None
    # Initialize with an infinite value for comparison.
    smallest_starship_size = float("inf")

    # Iterate over each starship and check if it appears in the first film.
    for starship in api_starships_data["results"]:
        # Fetch the film data
        films: List[Any] = [
            __get_request(film_url).json() for film_url in starship["films"]
        ]
        # Check if "A New Hope" appears in any of the films
        if any("A New Hope" in film["title"] for film in films):
            # Compare the length of the starship with the current smallest size.
            STARSHIP_VALID_FLOAT = float(starship["length"].replace(",", ""))
            if STARSHIP_VALID_FLOAT < smallest_starship_size:
                smallest_starship_size = STARSHIP_VALID_FLOAT
                smallest_starship_name = starship["name"]

    # log the name of the smallest starship in the first film.
    logger.info(smallest_starship_name)

    # Set the global string variable by replacing placeholders with provided answers.
    var.global_str = (
        var.global_str. \
        replace("<ans.1>", str(arid_films_values))
        .replace("<ans.2>", str(wookie_count))
        .replace("<ans.3>", str(smallest_starship_name))
    )

    logger_specials.value_was_set("var.global_str", f"\n{var.global_str}\n")

    clear_terminal()
    prt(var.global_str)

    return 0
