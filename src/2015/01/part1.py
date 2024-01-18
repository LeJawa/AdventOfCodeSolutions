######################################
# Solution for part 1 of day 01/2015 #
#                                    #
#  Started:     2024/01/18           #
#  Finished:    2024/01/18           #
######################################

from src.common.load_file import load_file

year, day = 2015, 1
input: list[str] = load_file(year, day)

def run() -> None:
    result = 0
    for c in input[0]:
        if c == "(":
            result += 1
        else:
            result -= 1
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}")
