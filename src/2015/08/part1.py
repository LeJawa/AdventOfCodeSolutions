######################################
# Solution for part 1 of day 08/2015 #
#                                    #
#  Started:     2024/02/25           #
#  Finished:    2024/02/25           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 8
input: list[str] = load_file(year, day)

def run() -> None:
    result = 0
    
    code_length = 0
    value_length = 0
    
    n = 1
    for line in input:
        string = line.strip()[1:-1]
        code_length_i = len(string) + 2
        
        modifier = -2
        i = -1
        while i < len(string) - 1:
            i += 1
            if string[i] != "\\":
                continue
            
            c = string[i + 1]
            if c == "\"" or c == "\\":
                modifier -= 1
                i += 1
                continue
            
            if c == "x":
                modifier -= 3
                i + 3
                continue
            
            print("c")
        
        value_length_i = code_length_i + modifier
        
        code_length += code_length_i
        value_length += value_length_i
        
        n += 1
        
    result = code_length - value_length
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
