######################################
# Solution for part 1 of day 03/2015 #
#                                    #
#  Started:     2024/01/19           #
#  Finished:    2024/01/19           #
######################################

from src.common.load_file import load_file

year, day = 2015, 3
input: list[str] = load_file(year, day)

class UniqueLocations:
    def __init__(self):
        self.locations: dict[int, dict[int, bool]] = {}
        self.total = 0
    
    def add(self, x: int, y: int):
        if (not x in self.locations.keys()):
            self.locations[x] = {}
        
        if (not y in self.locations[x]):
            self.total += 1

        self.locations[x][y] = True
        

def run() -> None:    
    visited_houses = UniqueLocations()
    
    x = 0
    y = 0
    visited_houses.add(x, y)
    for direction in input[0]:
        if direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        elif direction == "v":
            y -= 1
        else: # direction == "^"
            y += 1
        visited_houses.add(x,y)
    
    result = visited_houses.total
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
