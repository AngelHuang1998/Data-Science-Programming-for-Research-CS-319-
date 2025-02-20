"""
Reads data from steam.csv and provides public functions for students
to use to interact with this data without needing to know how to load
and manipulate CSV files.

There's a row for each game that contains these columns:
- name
- publisher
- release_date
- avg_playtime
- price
- positive_reviews
- negative_reviews
"""

from typing import List, Dict
import csv


_games: List[Dict[str, str]] = []


with open("steam.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        _games.append(row)


def count() -> int:
    """The number of games in the dataset"""

    return len(_games)


def get_name(idx: int) -> str:
    """The name of the game at row idx"""

    return _games[idx]["name"]


def get_publisher(idx: int) -> str:
    """The publisher of the game in row idx"""

    return _games[idx]["publisher"]


def get_release_date(idx: int) -> str:
    """The release date of the game in row idx in mm/dd/yyyy format"""

    return _games[idx]["release_date"]


def get_avg_playtime(idx: int) -> int:
    """The average playtime (in hours) of the game at row idx"""

    return int(_games[idx]["avg_playtime"])


def get_price(idx: int) -> str:
    """The price of the game at row idx, like $19.99"""

    return _games[idx]["price"]


def get_positive_reviews(idx: int) -> str:
    """The number of positive reviews for the game at row idx, like 2.81K"""

    return _games[idx]["positive_reviews"]


def get_negative_reviews(idx: int) -> str:
    """The number of negative reviews for the game at row idx, like 1.13K"""

    return _games[idx]["negative_reviews"]
