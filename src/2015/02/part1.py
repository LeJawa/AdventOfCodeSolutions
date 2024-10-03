######################################
# Solution for part 1 of day 02/2015 #
#                                    #
#  Started:     2024/01/18           #
#  Finished:    2024/01/18           #
######################################

from src.common.load_file import load_file

year, day = 2015, 2
input: list[str] = load_file(year, day)


def run() -> None:
    result = 0
    for gift in input:
        l, w, h = [int(x) for x in gift.strip().split("x")]

        result += 2 * (l * w + l * h + w * h)
        result += min(l * w, l * h, w * h)

    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}")
