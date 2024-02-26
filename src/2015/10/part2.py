######################################
# Solution for part 2 of day 10/2015 #
#                                    #
#  Started:     2024/02/26           #
#  Finished:    2024/02/26           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 10
input: list[str] = load_file(year, day)

def run() -> None:
    look_n_say = import_function(2015, 10, 1, "look_n_say")
    
    number = input[0].strip()
    
    for _ in range(50):
        number = look_n_say(number)   
    
    result = len(number)
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
