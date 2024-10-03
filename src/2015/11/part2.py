######################################
# Solution for part 2 of day 11/2015 #
#                                    #
#  Started:     2024/03/03           #
#  Finished:    2024/03/03           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function

year, day = 2015, 11
input: list[str] = load_file(year, day)


def run() -> None:
    check_password = import_function(year, day, 1, "check_password")
    get_next_password = import_function(year, day, 1, "get_next_password")

    password = input[0].strip()

    first_password_found = False

    while True:
        password = get_next_password(password)

        if check_password(password):
            if first_password_found:
                break

            first_password_found = True

    return password


if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
