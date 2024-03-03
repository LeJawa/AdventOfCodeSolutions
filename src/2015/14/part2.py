######################################
# Solution for part 2 of day 14/2015 #
#                                    #
#  Started:     2024/03/03           #
#  Finished:    2024/03/03           #
######################################

from dataclasses import dataclass
from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 14
input: list[str] = load_file(year, day)

@dataclass
class Reindeer:
    speed: int
    duration: int
    rest: int
    
    current_distance = 0
    flying = True
    flight_time = 0
    rest_time = 0
    
    points = 0
    
    def get_next_second_distance(self):
        if self.flying:
            if self.flight_time < self.duration:
                self.current_distance += self.speed
                self.flight_time += 1
            else:
                self.flying = False
                self.flight_time = 0
                self.rest_time += 1
        else:
            if self.rest_time < self.rest:
                self.rest_time += 1
            else:
                self.flying = True
                self.rest_time = 0
                self.flight_time += 1
                self.current_distance += self.speed
            
        return self.current_distance
    

def get_reindeers(input: list[str]) -> list[Reindeer]:
    deers = []
    
    for line in input:
        splits = line.split()
        
        deers.append(Reindeer(int(splits[3]), int(splits[6]), int(splits[-2])))
    
    return deers

def run() -> None:
    race_length = 2503
    
    deers = get_reindeers(input)
    
    for _ in range(race_length):
        max_distance = 0
        for deer in deers:
            distance = deer.get_next_second_distance()
            if distance > max_distance:
                max_distance = distance
                
        for deer in deers:
            if deer.current_distance == max_distance:
                deer.points += 1
        
    
    max_points = 0
    for deer in deers:
        if deer.points > max_points:
            max_points = deer.points
    
    result = max_points
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
