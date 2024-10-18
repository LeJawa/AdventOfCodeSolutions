######################################
# Solution for part 1 of day 14/2015 #
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

    def distance_after_x_seconds(self, x: int) -> int:
        flying = True

        distance = 0

        while x > 0:
            if flying:
                if x > self.duration:
                    distance += self.speed * self.duration
                else:
                    distance += self.speed * x
                flying = False
                x -= self.duration
            else:
                x -= self.rest
                flying = True

        return distance


def get_reindeers(input: list[str]) -> list[Reindeer]:
    deers = []

    for line in input:
        splits = line.split()

        deers.append(Reindeer(int(splits[3]), int(splits[6]), int(splits[-2])))

    return deers


def run() -> None:
    race_length = 2503

    deers = get_reindeers(input)

    distances = []
    for deer in deers:
        distances.append(deer.distance_after_x_seconds(race_length))

    result = max(distances)

    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
