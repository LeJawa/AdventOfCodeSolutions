######################################
# Solution for part 2 of day 16/2015 #
#                                    #
#  Started:     2024/08/22           #
#  Finished:    2024/08/22           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 16
input: list[str] = load_file(year, day)

mfcsam_result = import_function(2015, 16, 1, "mfcsam_result")
parse_sues = import_function(2015, 16, 1, "parse_sues")


def run() -> None:
    sues: list[dict] = parse_sues(input)
    for i, sue in enumerate(sues):
        sue_number = i + 1
        for key in sue.keys():
            if key == "cats" or key == "trees":
                if sue[key] <= mfcsam_result[key]:
                    sue_number = -1
                    break
            elif key == "pomeranians" or key == "goldfish":
                if sue[key] >= mfcsam_result[key]:
                    sue_number = -1
                    break
            else:
                if sue[key] != mfcsam_result[key]:
                    sue_number = -1
                    break
        if sue_number != -1:
            result = sue_number
            break
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
