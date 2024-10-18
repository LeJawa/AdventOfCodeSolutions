from importlib import import_module
from src.common.parsers import parse_year, parse_day


def import_function(year: str | int, day: str | int, part: str | int, function: str):
    year = parse_year(year)
    day = parse_day(day)

    return eval(f'import_module("src.{year}.{day:02d}.part{part}").{function}')
