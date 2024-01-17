import sys
from pathlib import Path
from src.common.parsers import parse_year, parse_day


def create_day(year: str, day: str) -> None:
    try:
        year = parse_year(year)
        day = parse_day(day)
    except ValueError as e:
        print(e)
        sys.exit(1)
    
    Path(f"src/{year}/{day:02d}").mkdir(parents=True, exist_ok=True)    
    Path(f"input/{year}").mkdir(parents=True, exist_ok=True)
    Path(f"input/{year}/{day:02d}.txt").touch()
    
    create_part_file(year, day, 1)
    create_part_file(year, day, 2)
    
    
    
    
def create_part_file(year: int, day: int, part: int) -> None:
    with open(f"src/{year}/{day:02d}/part{part}.py", "w") as f:
        f.write( "######################################\n")
        f.write(f"# Solution for part {part} of day {day:02d}/{year} #\n")
        f.write( "######################################\n\n")
        
        f.write("from src.common.load_file import load_file\n\n")
        
        f.write(f"year, day = {year}, {day}\n")
        f.write("input: list[str] = load_file(year, day)\n\n")
        
        f.write(f"def part{part}() -> None:\n")
        f.write("    pass\n\n")
        
        f.write("if __name__ == \"__main__\":\n")
        f.write(f"    part{part}()\n")