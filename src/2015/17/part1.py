######################################
# Solution for part 1 of day 17/2015 #
#                                    #
#  Started:     2024/08/23           #
#  Finished:    2024/08/24           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 17
input: list[str] = load_file(year, day)

EGGNOG_AMOUNT = 150

# Taken from https://docs.python.org/3/library/itertools.html#itertools.combinations
# Not one of my finest moments...
def combinations(containers: list[int], r: int):
    sorted_containers = [*containers]
    sorted_containers.sort()
    n = len(sorted_containers)
    if r > n:
        return
    indices = list(range(r))

    l = 0

    s = 0
    for i in indices:
        s += sorted_containers[i]
    
    if s > EGGNOG_AMOUNT: # Only possible because pool is sorted
        return l
    
    if s == EGGNOG_AMOUNT:
        l += 1
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return l
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        
        s = 0
        for i in indices:
            s += sorted_containers[i]
        if s == EGGNOG_AMOUNT:
            l += 1


def run() -> None:
    containers: list[int] = []
    for line in input:
        containers.append(int(line.strip()))

    containers.sort()
    ways = 0
    for i in range(len(containers)):
        ways += combinations(containers, i + 1)

    result = ways

    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
