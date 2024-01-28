######################################
# Solution for part 2 of day 06/2015 #
#                                    #
#  Started:     2024/01/28           #
#  Finished:    2024/01/28           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function
import re

year, day = 2015, 6
input: list[str] = load_file(year, day)

def run() -> None:
    result = 0
    size = 1000
    
    instruction_pattern = r"(toggle|turn off|turn on) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})"
    
    grid: list[list[int]] = [[0 for x in range(size)] for y in range(size)]
    
    for line in input:
        instruction, from_x, from_y, to_x, to_y = re.match(instruction_pattern, line).groups()
        
        from_x = int(from_x)
        from_y = int(from_y)
        to_x = int(to_x)
        to_y = int(to_y)     
        
        for y in range(from_y, to_y + 1):
            for x in range(from_x, to_x +1):
                if instruction == "turn on":
                    grid[y][x] += 1
                elif instruction == "turn off":
                    grid[y][x] += -1 if grid[y][x] > 0 else 0
                else: # instruction == "toggle"
                    grid[y][x] += 2
    
    
    for y in range(size):
        for x in range(size):
            result += grid[y][x]
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
