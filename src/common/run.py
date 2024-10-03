import sys
from src.common.globals import LAST_YEAR
from src.common.parsers import parse_year

from importlib import import_module


def run_all_years():
    for year in range(2015, LAST_YEAR + 1):
        run_year(str(year))


def run_year(year: str):
    try:
        year = parse_year(year)
    except ValueError as e:
        print(e)
        sys.exit(1)

    for day in range(1, 26):
        run_day(year, day)


def run_day(year: int, day: int) -> None:
    print(f"Running year {year}, day {day}")

    part1 = import_module(f"src.{year}.{day:02d}.part1")
    part2 = import_module(f"src.{year}.{day:02d}.part2")

    print(f"Part 1 - Result: {part1.run()}")
    print(f"Part 2  - Result: {part2.run()}\n")
