######################################
# Solution for part 1 of day 16/2015 #
#                                    #
#  Started:     2024/08/22           #
#  Finished:    2024/08/22           #
######################################

from ast import parse
import re
from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 16
input: list[str] = load_file(year, day)

mfcsam_result = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse_sues(input: list[str]):
    sues: list[dict] = []
    for line in input:
        matches = re.match(
            r"Sue (\d+): (.+): (\d+), (.+): (\d+), (.+): (\d+)", line
        ).groups()
        sues.append(
            {
                matches[1]: int(matches[2]),
                matches[3]: int(matches[4]),
                matches[5]: int(matches[6]),
            }
        )
    return sues


def run() -> None:
    sues: list[dict] = parse_sues(input)
    for i, sue in enumerate(sues):
        sue_number = i + 1
        for key in sue.keys():
            if sue[key] != mfcsam_result[key]:
                sue_number = -1
                break
        if sue_number != -1:
            result = sue_number
            break

    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
