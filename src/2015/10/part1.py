######################################
# Solution for part 1 of day 10/2015 #
#                                    #
#  Started:     2024/02/26           #
#  Finished:    2024/02/26           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 10
input: list[str] = load_file(year, day)


def look_n_say(number: str) -> str:

    result = ""

    count = 0
    for i in range(len(number)):
        c = number[i]

        if i < len(number) - 1:
            next_c = number[i + 1]
        else:
            next_c = "END"

        count += 1

        if c != next_c:
            result += str(count) + c
            count = 0

    return result


def run() -> None:
    number = input[0].strip()

    for _ in range(40):
        number = look_n_say(number)

    result = len(number)

    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
