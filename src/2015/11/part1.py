######################################
# Solution for part 1 of day 11/2015 #
#                                    #
#  Started:     2024/03/03           #
#  Finished:    2024/03/03           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 11
input: list[str] = load_file(year, day)

def get_next_password(old_password: str) -> str:
    new_password = ""
    incrementing = True
    for c in old_password[::-1]:
        next_ord = ord(c)
        if incrementing:
            next_ord += 1
            if next_ord == 123:
                next_ord = 97
                incrementing = True
            else:
                incrementing = False

        new_password += chr(next_ord)
    
    return new_password[::-1]

def check_password(password: str) -> bool:
    
    previous_char = ''    
    
    one_pair_found = False
    two_pairs_found = False
    overlapping_pair = False
    
    three_straight_found = False
    two_straight_going = False
    
    for c in password:
        if c == "i" or c == "o" or c == "l":
            return False
        
        if previous_char == '':
            previous_char = c
            continue        
        
        if c == previous_char:
            two_straight_going = False
            
            if not overlapping_pair:
                if one_pair_found:
                    two_pairs_found = True
                else:
                    one_pair_found = True
                    overlapping_pair = True
            else:
                overlapping_pair = False
                
        else:
            overlapping_pair = False
            
            if ord(c) == ord(previous_char) + 1:
                if two_straight_going:
                    three_straight_found = True
                else:
                    two_straight_going = True
            else:
                two_straight_going = False
        
        previous_char = c
        
    return three_straight_found and two_pairs_found


def run() -> None:
    password = input[0].strip()
    
    while(not check_password(password)):
        password = get_next_password(password)
        
    return password


if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
