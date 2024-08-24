######################################
# Solution for part 2 of day 17/2015 #
#                                    #
#  Started:     2024/08/23           #
#  Finished:    ----/--/--           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 17
input: list[str] = load_file(year, day)

combinations = import_function(2015, 17, 1, "combinations")

def run() -> None:
    containers: list[int] = []
    for line in input:
        containers.append(int(line.strip()))

    containers.sort()
    ways = 0
    for i in range(len(containers)):
        ways = combinations(containers, i + 1)
        if ways > 0:
            break

    result = ways
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
