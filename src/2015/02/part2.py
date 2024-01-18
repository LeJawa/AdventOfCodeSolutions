######################################
# Solution for part 2 of day 02/2015 #
#                                    #
#  Started:     2024/01/18           #
#  Finished:    2024/01/18           #
######################################

from src.common.load_file import load_file

year, day = 2015, 2
input: list[str] = load_file(year, day)

def run() -> None:
    result = 0
    for gift in input:
        l,w,h = [int(x) for x in gift.strip().split("x")]
        
        result += l*w*h
        result += l+l+w+w+h+h
        result -= 2*max(l,w,h)    
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}")
