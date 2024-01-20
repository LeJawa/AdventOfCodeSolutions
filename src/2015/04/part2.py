######################################
# Solution for part 2 of day 04/2015 #
#                                    #
#  Started:     2024/01/20           #
#  Finished:    ----/--/--           #
######################################

from src.common.load_file import load_file
try:
    from part1 import get_number
except:
    from importlib import import_module
    get_number = import_module("src.2015.04.part1").get_number


year, day = 2015, 4
input: list[str] = load_file(year, day)

def run() -> None:
    result = get_number(6)
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
