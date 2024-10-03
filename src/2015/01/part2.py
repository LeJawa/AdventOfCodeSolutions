######################################
# Solution for part 2 of day 01/2015 #
#                                    #
#  Started:     2024/01/18           #
#  Finished:    2024/01/18           #
######################################

from src.common.load_file import load_file

year, day = 2015, 1
input: list[str] = load_file(year, day)


def run() -> None:
    result = 0
    for index, c in enumerate(input[0]):
        if result == -1:
            result = index
            break

        if c == "(":
            result += 1
        else:
            result -= 1

    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}")
