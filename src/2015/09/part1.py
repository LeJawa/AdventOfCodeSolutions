######################################
# Solution for part 1 of day 09/2015 #
#                                    #
#  Started:     2024/02/25           #
#  Finished:    2024/02/25           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function
import copy

year, day = 2015, 9
input: list[str] = load_file(year, day)

### Calculates the shortest path from source to target, while going through all the cities in set
def bhk(group: list[str], source: str, target: str, distance_dict: dict[str, dict[str, int]], minimize = True) -> int :
    if len(group) == 0:
        return distance_dict[source][target]    
    
    distances: list[int] = []
    for city in group:    
        new_group = list(group)
        new_group.remove(city)
        
        distances.append(bhk(new_group, source, city, distance_dict, minimize) + distance_dict[city][target])
    
    return min(distances) if minimize else max(distances)

def get_best_path_length(distance_dict: dict[str, dict[str, int]], minimize = True) -> int:
    cities = list(distance_dict.keys())
    
    distances: list[int] = []
    for source in cities:
        for target in cities:
            if source == target:
                continue
            group = list(cities)
            group.remove(source)
            group.remove(target)
            distances.append(bhk(group, source, target, distance_dict, minimize))
    
    return min(distances) if minimize else max(distances)

def parse_distances(input: list[str]) -> dict[str, dict[str, int]]:
    distance_dict: dict[str, dict[str, int]] = {}
    
    for line in input:
        from_city, _, to_city, _, distance = line.split()
        
        try:
            distance_dict[from_city][to_city] = int(distance)
        except:
            distance_dict[from_city] = {to_city: int(distance)}
        try:
            distance_dict[to_city][from_city] = int(distance)
        except:
            distance_dict[to_city] = {from_city: int(distance)}
    
    return distance_dict

def run() -> None:
    distance_dict = parse_distances(input)    
            
    result = get_best_path_length(distance_dict)
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
