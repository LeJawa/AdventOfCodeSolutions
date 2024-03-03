######################################
# Solution for part 2 of day 13/2015 #
#                                    #
#  Started:     2024/03/03           #
#  Finished:    2024/03/03           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 13
input: list[str] = load_file(year, day)

def run() -> None:
    get_happiness_dict = import_function(year, day, 1, "get_happiness_dict")
    modified_bhk = import_function(year, day, 1, "modified_bhk")
    
    result = 0    
    happiness = get_happiness_dict(input)
    
    names = list(happiness.keys())
    
    me = "me"
    happiness[me] = {}
    
    for name in names:
        happiness[name][me] = 0
        happiness[me][name] = 0
    
    result = modified_bhk(names, me, me, happiness, False)    
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
