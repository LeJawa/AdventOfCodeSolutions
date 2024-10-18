######################################
# Solution for part 1 of day 13/2015 #
#                                    #
#  Started:     2024/03/03           #
#  Finished:    2024/03/03           #
######################################

from src.common.load_file import load_file, load_test_file
from src.common.function_import import import_function

year, day = 2015, 13
input: list[str] = load_file(year, day)


def modified_bhk(
    group: list[str],
    source: str,
    target: str,
    distance_dict: dict[str, dict[str, int]],
    minimize=True,
) -> int:
    if len(group) == 0:
        return distance_dict[source][target] + distance_dict[target][source]

    distances: list[int] = []
    for city in group:
        new_group = list(group)
        new_group.remove(city)

        distances.append(
            modified_bhk(new_group, source, city, distance_dict, minimize)
            + distance_dict[city][target]
            + distance_dict[target][city]
        )

    return min(distances) if minimize else max(distances)


def get_happiness_dict(input: list[str]) -> dict[str, dict[str, int]]:
    happiness = {}

    for line in input:
        splits = line[0:-2].split()

        try:
            happiness[splits[0]][splits[-1]] = (
                int(splits[3]) if splits[2] == "gain" else -int(splits[3])
            )
        except:
            happiness[splits[0]] = {
                splits[-1]: int(splits[3]) if splits[2] == "gain" else -int(splits[3])
            }

    return happiness


def run() -> None:
    result = 0
    happiness = get_happiness_dict(input)

    names = list(happiness.keys())
    first_name = names.pop()

    result = modified_bhk(names, first_name, first_name, happiness, False)

    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
