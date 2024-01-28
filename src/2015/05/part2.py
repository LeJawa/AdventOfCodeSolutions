######################################
# Solution for part 2 of day 05/2015 #
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
    pairs = r"([a-z]{2}).*\1"
    separated = r"([a-z]).\1"
    
    for line in [l.strip() for l in input]:
        if re.search(pairs, line, ) and re.search(separated, line):
            result += 1    
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
