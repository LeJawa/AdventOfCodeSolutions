######################################
# Solution for part 1 of day 15/2015 #
#                                    #
#  Started:     2024/03/03           #
#  Finished:    2024/08/22           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function
import re

year, day = 2015, 15
input: list[str] = load_file(year, day)


def get_score(
    i: int, j: int, k: int, l: int, ingredients: list[tuple[int, int, int, int]]
) -> int:
    c = (
        i * ingredients[0][0]
        + j * ingredients[1][0]
        + k * ingredients[2][0]
        + l * ingredients[3][0]
    )
    d = (
        i * ingredients[0][1]
        + j * ingredients[1][1]
        + k * ingredients[2][1]
        + l * ingredients[3][1]
    )
    f = (
        i * ingredients[0][2]
        + j * ingredients[1][2]
        + k * ingredients[2][2]
        + l * ingredients[3][2]
    )
    t = (
        i * ingredients[0][3]
        + j * ingredients[1][3]
        + k * ingredients[2][3]
        + l * ingredients[3][3]
    )

    return c * d * f * t if c > 0 and d > 0 and f > 0 and t > 0 else 0


def brute_force(ingredients: list[tuple[int, int, int, int]]):
    if len(ingredients) != 4:
        return 0

    max_score = -1

    for i in range(100):
        for j in range(100):
            if i + j > 100:
                break
            for k in range(100):
                if i + j + k > 100:
                    break
                l = 100 - (i + j + k)

                score = get_score(i, j, k, l, ingredients)
                if score > max_score:
                    max_score = score

    return max_score


def run() -> None:
    ingredients: list[tuple[int, int, int, int]] = []
    for line in input:
        c, d, f, t = re.match(
            r".*: capacity (.+), durability (.+), flavor (.+), texture (.+),", line
        ).groups()
        ingredients.append((int(c), int(d), int(f), int(t)))

    result = brute_force(ingredients)

    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
