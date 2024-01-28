######################################
# Solution for part 2 of day 04/2015 #
#                                    #
#  Started:     2024/01/20           #
#  Finished:    2024/01/20           #
#  Improved:    2024/01/28           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 4
input: list[str] = load_file(year, day)

get_number = import_function(year, day, 1, "get_number")

def run() -> None:
    result = get_number(input[0], 6)
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
