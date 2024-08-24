######################################
# Solution for part 2 of day 18/2015 #
#                                    #
#  Started:     2024/08/24           #
#  Finished:    2024/08/24           #
######################################

from src.common.load_file import load_file, load_test_file
from src.common.function_import import import_function

parse_input = import_function(2015, 18, 1, "parse_input")
print_lights = import_function(2015, 18, 1, "print_lights")

year, day = 2015, 18
input: list[str] = load_file(year, day)

STEPS = 100

def run() -> None:
    lights = parse_input(input)
    
    GRID_SIZE = len(lights)
    
    # Set stuck lights on
    lights[0][0] = True
    lights[0][GRID_SIZE - 1] = True
    lights[GRID_SIZE - 1][0] = True
    lights[GRID_SIZE - 1][GRID_SIZE - 1] = True
    
    # print_lights(lights, 0)

    for step in range(STEPS):
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
                lights[y][x] = (
                    neighbors[y][x] == 3
                    or (neighbors[y][x] == 2 and lights[y][x])
                    or (x == 0 and y == 0)
                    or (x == 0 and y == GRID_SIZE - 1)
                    or (x == GRID_SIZE - 1 and y == 0)
                    or (x == GRID_SIZE - 1 and y == GRID_SIZE - 1)
                )
                lights_on += 1 if lights[y][x] else 0
        
        # print_lights(lights, step + 1)

    result = lights_on

    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
