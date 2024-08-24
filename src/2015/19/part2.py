######################################
# Solution for part 2 of day 19/2015 #
#                                    #
#  Started:     2024/08/24           #
#  Finished:    ----/--/--           #
######################################

from src.common.load_file import load_file, load_test_file
from src.common.function_import import import_function

from typing import Callable

parse_input: Callable[[list[str]], tuple[list[tuple[str, str]], str]]
parse_input = import_function(2015, 19, 1, "parse_input")

year, day = 2015, 19
input: list[str] = load_test_file(year, day)

def run() -> None:    
    replacements, final_molecule = parse_input(input)
    
    
    print(replacements)
    print(final_molecule)
    
    
    result = 0
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
