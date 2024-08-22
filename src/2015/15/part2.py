######################################
# Solution for part 2 of day 15/2015 #
#                                    #
#  Started:     2024/08/22           #
#  Finished:    2024/08/22           #
######################################

import re
from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 15
input: list[str] = load_file(year, day)

get_score = import_function(2015, 15, 1, "get_score")


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

                calories = (
                    i * ingredients[0][4]
                    + j * ingredients[1][4]
                    + k * ingredients[2][4]
                    + l * ingredients[3][4]
                )
                if calories != 500:
                    break

                score = get_score(i, j, k, l, ingredients)
                if score > max_score:
                    max_score = score

    return max_score


def run() -> None:
    ingredients: list[tuple[int, int, int, int]] = []
    for line in input:
        c, d, f, t, cal = re.match(
            r".*: capacity (.+), durability (.+), flavor (.+), texture (.+), calories (.+)",
            line,
        ).groups()
        ingredients.append((int(c), int(d), int(f), int(t), int(cal)))

    result = brute_force(ingredients)

    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
