######################################
# Solution for part 1 of day 19/2015 #
#                                    #
#  Started:     2024/08/24           #
#  Finished:    2024/08/24           #
######################################

import re
from src.common.load_file import load_file, load_test_file
from src.common.function_import import import_function

year, day = 2015, 19
input: list[str] = load_file(year, day)

def parse_input(input:list[str]) -> tuple[list[tuple[str, str]], str]:
    replacements: list[tuple[str, str]] = []
    for line in input:
        if line != "\n":
            if "=>" in line:
                key, value = re.match(
                        r"(.+) => (.+)", line.strip()
                    ).groups()
                
                replacements.append((key, value))
            else:
                molecule = line.strip()
    
    return (replacements, molecule)

def run() -> None:
    replacements, initial_molecule = parse_input(input)
    
    molecule_set: set = set()
    
    for replacement in replacements:
        index = 0
        while True:
            index = initial_molecule.find(replacement[0], index)
            
            if index == -1:
                break
            
            molecule = initial_molecule[:index] + initial_molecule[index:].replace(replacement[0], replacement[1], 1)
            
            molecule_set.add(molecule)
            index += 1
            
    result = len(molecule_set)
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
