######################################
# Solution for part 2 of day 08/2015 #
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
    encoded_length = 0
    
    for line in input:
        string = line.strip()
        code_length_i = len(string)
        encoded_length_i = code_length_i + 2
        
        for c in string:
            encoded_length_i += 1 if c == "\"" or c == "\\" else 0
            
        code_length += code_length_i
        encoded_length += encoded_length_i
    
    result = encoded_length - code_length
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
