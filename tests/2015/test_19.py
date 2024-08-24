from importlib import import_module

part1 = import_module("src.2015.19.part1")
part2 = import_module("src.2015.19.part2")
answer_file = "answers/2015/19.txt"

part1_answer = None
part2_answer = None

def test_get_part1_answer() -> str:
    with open(answer_file, "r") as f:
        try:
            part1_answer = f.readline().strip()
        except Exception as e:
            pass

    assert part1_answer is not None
    return part1_answer

def test_get_part2_answer() -> str:
    with open(answer_file, "r") as f:
        try:
            _ = f.readline().strip()
            part2_answer = f.readline().strip()
        except Exception as e:
            pass

    assert part2_answer is not None
    return part2_answer

def test_part1() -> None:
    assert part1.run() == test_get_part1_answer()

def test_part2() -> None:
    assert part2.run() == test_get_part2_answer()
