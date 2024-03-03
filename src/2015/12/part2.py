######################################
# Solution for part 2 of day 12/2015 #
#                                    #
#  Started:     2024/03/03           #
#  Finished:    2024/03/03           #
######################################

import json
from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 12
input: list[str] = load_file(year, day)


def get_list_sum(lst: list) -> int:    
    total = 0
    
    for item in lst:
        total += get_value(item)
    
    return total

def get_value(value) -> int:
    if isinstance(value, dict):
        return get_obj_sum(value)
    elif isinstance(value, list):
        return get_list_sum(value)
    
    try:
        return int(value)
    except:
        return 0

def get_obj_sum(obj: dict) -> int:
    total = 0

    for key in obj.keys():
        if obj[key] == "red":
            return 0
            
        total += get_value(obj[key])

    return total

def run() -> None:
    obj = json.loads(input[0].strip())

    result = get_obj_sum(obj)
    
    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
