import sys
from pathlib import Path
from src.common.parsers import parse_year, parse_day
from datetime import datetime


def create_day(year: str, day: str) -> None:
    try:
        year = parse_year(year)
        day = parse_day(day)
    except ValueError as e:
        print(e)
        raise ValueError("Error parsing year or day.")

    # src
    Path(f"src/{year}/{day:02d}").mkdir(parents=True, exist_ok=True)
    create_part_file(year, day, 1)
    create_part_file(year, day, 2)

    # input
    Path(f"input/{year}").mkdir(parents=True, exist_ok=True)
    Path(f"input/{year}/{day:02d}.txt").touch()

    # answers
    Path(f"answers/{year}").mkdir(parents=True, exist_ok=True)
    Path(f"answers/{year}/{day:02d}.txt").touch()

    # tests
    Path(f"tests/{year}").mkdir(parents=True, exist_ok=True)
    create_test_file(year, day)

    print(f"\n> Files created for day {day:02d} of year {year}\n")


def create_part_file(year: int, day: int, part: int) -> None:
    part_file = f"src/{year}/{day:02d}/part{part}.py"
    if Path(part_file).exists():
        print(f"{part_file} already exists")
        return

    current_date = datetime.now().strftime("%Y/%m/%d")

    with open(part_file, "w") as f:
        f.write("######################################\n")
        f.write(f"# Solution for part {part} of day {day:02d}/{year} #\n")
        f.write(f"#                                    #\n")
        f.write(f"#  Started:     {current_date}           #\n")
        f.write(f"#  Finished:    ----/--/--           #\n")
        f.write("######################################\n\n")

        f.write("from src.common.load_file import load_file\n")
        f.write("from src.common.function_import import import_function\n\n")

        f.write(f"year, day = {year}, {day}\n")
        f.write("input: list[str] = load_file(year, day)\n\n")

        f.write("def run() -> None:\n")
        f.write("    result = 0\n    \n    \n    \n")

        f.write("    return str(result)\n\n")

        f.write('if __name__ == "__main__":\n')
        f.write("    result = run()\n")
        f.write(
            f'    print(f"Part {part} day {{day}} - {{year}}\\nResult: {{result}}\\n")\n'
        )


def create_test_file(year: int, day: int) -> None:
    test_file = f"tests/{year}/test_{day:02d}.py"
    if Path(test_file).exists():
        print(f"{test_file} already exists")
        return

    with open(test_file, "w") as f:
        f.write("from importlib import import_module\n\n")

        f.write(f'part1 = import_module("src.{year}.{day:02d}.part1")\n')
        f.write(f'part2 = import_module("src.{year}.{day:02d}.part2")\n')

        f.write(f'answer_file = "answers/{year}/{day:02d}.txt"\n\n')

        f.write("part1_answer = None\n")
        f.write("part2_answer = None\n\n")

        f.write("def test_get_part1_answer() -> str:\n")
        f.write('    with open(answer_file, "r") as f:\n')
        f.write("        try:\n")
        f.write("            part1_answer = f.readline().strip()\n")
        f.write("        except Exception as e:\n")
        f.write("            pass\n\n")

        f.write("    assert part1_answer is not None\n")
        f.write("    return part1_answer\n\n")

        f.write("def test_get_part2_answer() -> str:\n")
        f.write('    with open(answer_file, "r") as f:\n')
        f.write("        try:\n")
        f.write("            _ = f.readline().strip()\n")
        f.write("            part2_answer = f.readline().strip()\n")
        f.write("        except Exception as e:\n")
        f.write("            pass\n\n")

        f.write("    assert part2_answer is not None\n")
        f.write("    return part2_answer\n\n")

        f.write("def test_part1() -> None:\n")
        f.write("    assert part1.run() == test_get_part1_answer()\n\n")

        f.write("def test_part2() -> None:\n")
        f.write("    assert part2.run() == test_get_part2_answer()\n")
