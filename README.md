# Math Genealogy Scraper (Django Web App)

This is a Django-based web application that builds and displays the academic ancestor tree for any individual listed in the Mathematics Genealogy Project. It fetches advisor information recursively and displays the result in a structured text format on a webpage.

## Features

- Web interface for querying any Math Genealogy ID
- Displays the tree of intellectual ancestors up to a user-defined depth
- Shows the name of the mathematician at the top of the result
- Backend caching to avoid redundant network requests
- Recursive tree building with safety depth limits

## Requirements

- Python 3.7+
- pip
- Internet connection (the tool scrapes live data from https://genealogy.math.ndsu.nodak.edu)
- django, requests, beautifulsoup4, certifi

## Setup

Simply run the manage.py file in the mathgen_project directory with parameter "runserver".
