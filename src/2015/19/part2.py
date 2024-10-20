######################################
# Solution for part 2 of day 19/2015 #
#                                    #
#  Started:     2024/10/18           #
#  Finished:    2024/10/20           #
######################################

import random
from src.common.load_file import load_file, load_test_file
from src.common.function_import import import_function

from typing import Callable

parse_input: Callable[[list[str]], tuple[list[tuple[str, str]], str]]
parse_input = import_function(2015, 19, 1, "parse_input")

year, day = 2015, 19
input: list[str] = load_file(year, day)
# input: list[str] = load_test_file(year, day)

def parse_replacements(replacements: list[tuple[str, str]]) -> dict[str, str]:
    replacement_dict = {}
    
    for r in replacements:
        if r[1] in replacement_dict.keys():
            print("error", r[1])
        replacement_dict[r[1]] = r[0]
    
    return replacement_dict

def run() -> None:
    replacements, final_molecule = parse_input(input)

    print(replacements)
    print(final_molecule)
    
    replacement_dict = parse_replacements(replacements)
    molecule = final_molecule
    
    keys = list(replacement_dict.keys())
    keys.sort(key=lambda x: len(x), reverse=True)
    
    steps = 0
    tries = 1
        
    while molecule != "e":
        didnt_find_key = True
        for key in keys:
            if key in molecule:
                molecule = molecule.replace(key, replacement_dict[key], 1)
                steps += 1
                didnt_find_key = False
                break
        
        if didnt_find_key:
            random.shuffle(keys)
            tries += 1
            steps = 0
            molecule = final_molecule
            continue            

    result = steps
    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
