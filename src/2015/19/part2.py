######################################
# Solution for part 2 of day 19/2015 #
#                                    #
#  Started:     2024/10/18           #
#  Finished:    ----/--/--           #
######################################

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

def reduce_molecule(molecule: str, replacement_dict: dict[str, str], steps) -> str:
    if molecule == "e":
        return steps
    
    for key in replacement_dict.keys():
        
        indices = []
        
        idx = molecule.find(key)
        
        while idx != -1:
            indices.append(idx)
            new_idx = molecule[idx+len(key):].find(key)
            if new_idx != -1:
                idx += new_idx + 1
            else:
                idx = -1
        
        for idx in indices:
            temp_molecule = molecule.replace(key, replacement_dict[key], 1)
            if replacement_dict[key] == "e" and temp_molecule != "e":
                continue
            else:
                result = reduce_molecule(temp_molecule, replacement_dict, steps+1)
                if result != -1:
                    return result
                # print(steps)
                

    return -1

def run() -> None:
    replacements, final_molecule = parse_input(input)

    print(replacements)
    print(final_molecule)
    
    replacement_dict = parse_replacements(replacements)
    molecule = "HCaCaF"
    
    steps = reduce_molecule(final_molecule, replacement_dict, 0)
    

    result = steps
    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
