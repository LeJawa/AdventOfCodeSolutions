######################################
# Solution for part 1 of day 05/2015 #
#                                    #
#  Started:     2024/01/28           #
#  Finished:    2024/01/28           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function
import re

year, day = 2015, 5
input: list[str] = load_file(year, day)

def run() -> None:
    result = 0
    vowels = r"[aeiou].*[aeiou].*[aeiou]"
    double = r"([a-z])\1"
    not_strings = r"(ab|cd|pq|xy)"
    
    for line in [l.strip() for l in input]:
        if re.search(vowels, line, ) and re.search(double, line) and not re.search(not_strings, line):
            result += 1    
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
