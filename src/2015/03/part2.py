######################################
# Solution for part 2 of day 03/2015 #
#                                    #
#  Started:     2024/01/19           #
#  Finished:    2024/01/19           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 3
input: list[str] = load_file(year, day)

UniqueLocations = import_function(year, day, 1, "UniqueLocations")


def run() -> None:
    visited_houses = UniqueLocations()

    rx, sx = 0, 0
    ry, sy = 0, 0

    santas_turn = True

    visited_houses.add(sx, sy)
    for direction in input[0]:
        if direction == ">":
            if santas_turn:
                sx += 1
            else:
                rx += 1
        elif direction == "<":
            if santas_turn:
                sx -= 1
            else:
                rx -= 1
        elif direction == "v":
            if santas_turn:
                sy -= 1
            else:
                ry -= 1
        else:  # direction == "^"
            if santas_turn:
                sy += 1
            else:
                ry += 1

        if santas_turn:
            visited_houses.add(sx, sy)
        else:
            visited_houses.add(rx, ry)

        santas_turn = not santas_turn

    result = visited_houses.total

    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
