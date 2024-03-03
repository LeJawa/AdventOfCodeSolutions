######################################
# Solution for part 1 of day 12/2015 #
#                                    #
#  Started:     2024/03/03           #
#  Finished:    2024/03/03           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 12
input: list[str] = load_file(year, day)


def run() -> None:

    result = 0
    str_number = ""

    for c in input[0]:
        if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]:
            if str_number != "":
                result += int(str_number)
                str_number = ""
            continue

        str_number += c

    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
