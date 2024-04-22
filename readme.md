# SWAPI Explorer API

This Python script retrieves data from the SWAPI (Star Wars API) and analyzes it to answer some interesting questions about the Star Wars universe.

**Functionality:**

- Finds the number of films featuring planets with an arid climate.
- Counts the total number of Wookiees across the saga.
- Identifies the name of the smallest starship that appears in the first film ("A New Hope").

**Requirements:**

- Python 3.x
- `requests` library (install using `pip install requests`)

**How to Use:**

1. Clone or download this repository.
2. Install the `requests` library: `pip install requests`
3. Run the script: `python main.py`

**Output:**

The script will print the following information to the console:

- The number of films featuring arid planets.
- The total number of Wookiees across the saga.
- The name of the smallest starship that appears in the first film.

**Dependencies:**

- This script relies on the `requests` library for making HTTP requests to the SWAPI API.

**License:**

This project is licensed under the MIT License - see the [license](license) file for details.

**Further Development:**

- Enhance error handling for potential issues with API requests or data parsing.
- Provide more informative output messages.
- Allow customization of the script's behavior through command-line arguments or configuration files.
- Consider integrating unit tests to ensure code reliability.
