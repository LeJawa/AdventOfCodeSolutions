######################################
# Solution for part 1 of day 18/2015 #
#                                    #
#  Started:     2024/08/24           #
#  Finished:    2024/08/24           #
######################################

from src.common.load_file import load_file, load_test_file
from src.common.function_import import import_function

year, day = 2015, 18
input: list[str] = load_file(year, day)

STEPS = 100


def parse_input(input: list[str]) -> list[list[bool]]:
    grid: list[list[bool]] = []
    for line in input:
        grid.append([c == "#" for c in list(line.strip())])
    return grid


def print_lights(lights: list[list[bool]], step: int = None):
    print()
    
    if step is not None:
        print(f"Step {step}:")
        
    n = len(lights)
    for x in range(n):
        print("".join(["#" if lights[x][i] else "." for i in range(n)]))


def run() -> None:
    lights = parse_input(input)
    # print_lights(lights)

    GRID_SIZE = len(lights)

    for _ in range(STEPS):
        neighbors = [[0 for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
        # print(neighbors)
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if lights[y][x]:
                    if y > 0:
                        neighbors[y - 1][x] += 1
                        if x > 0:
                            neighbors[y - 1][x - 1] += 1
                        if x < GRID_SIZE - 1:
                            neighbors[y - 1][x + 1] += 1
                    if y < GRID_SIZE - 1:
                        neighbors[y + 1][x] += 1
                        if x > 0:
                            neighbors[y + 1][x - 1] += 1
                        if x < GRID_SIZE - 1:
                            neighbors[y + 1][x + 1] += 1

                    if x > 0:
                        neighbors[y][x - 1] += 1
                    if x < GRID_SIZE - 1:
                        neighbors[y][x + 1] += 1

        lights_on = 0
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                lights[y][x] = neighbors[y][x] == 3 or (
                    neighbors[y][x] == 2 and lights[y][x]
                )
                lights_on += 1 if lights[y][x] else 0

    result = lights_on

    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
