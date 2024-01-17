from src.common.globals import LAST_YEAR


def parse_day(day: str) -> int:
    try:
        day = int(day)
        if day < 1 or day > 25:
            raise ValueError
    except ValueError:
        raise ValueError("Day must be a number between 1 and 25.")

    return day


def parse_year(year: str) -> int:
    try:
        if len(year) == 4:
            year = int(year)
            if year < 2015 or year > LAST_YEAR:
                raise ValueError
        elif len(year) == 2:
            year = int(year)
            if year < 15 or year > LAST_YEAR % 100:
                raise ValueError
            year += 2000
    except ValueError:
        raise ValueError("Year must be a number between 2015 and current year.")

    return year
