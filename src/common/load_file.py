def load_file(year: int, day: int) -> list[str]:
    with open(f"input/{year}/{day:02d}.txt") as f:
        return f.readlines()


def load_test_file(year: int, day: int, suffix: str = "_test") -> list[str]:
    with open(f"input/{year}/{day:02d}{suffix}.txt") as f:
        return f.readlines()
