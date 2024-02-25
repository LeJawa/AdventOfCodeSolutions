######################################
# Solution for part 2 of day 09/2015 #
#                                    #
#  Started:     2024/02/25           #
#  Finished:    2024/02/25           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 9
input: list[str] = load_file(year, day)

def run() -> None:
    parse_distances = import_function(2015, 9, 1, "parse_distances")
    get_best_path_length = import_function(2015, 9, 1, "get_best_path_length")    
    
    distance_dict = parse_distances(input)    
            
    result = get_best_path_length(distance_dict, False)
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
