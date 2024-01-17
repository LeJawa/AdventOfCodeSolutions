def load_file(year: int, day: int) -> list[str]:
    with open(f"input/{year}/{day:02d}.txt") as f:
        return f.readlines()