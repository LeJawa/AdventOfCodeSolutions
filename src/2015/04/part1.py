######################################
# Solution for part 1 of day 04/2015 #
#                                    #
#  Started:     2024/01/20           #
#  Finished:    ----/--/--           #
######################################

from src.common.load_file import load_file
from hashlib import md5

year, day = 2015, 4
input: list[str] = load_file(year, day)

def get_number(zeroes):
    number = -1
    prefix = input[0]    
    hash = "."*32
    
    while(hash[:zeroes] != "0"*zeroes):
        number += 1
        hash = md5( (prefix + str(number)).encode() ).hexdigest()
    
    return number
    

def run() -> None:
    result = get_number(5)
     
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
