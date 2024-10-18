######################################
# Solution for part 1 of day 04/2015 #
#                                    #
#  Started:     2024/01/20           #
#  Finished:    2024/01/20           #
#  Improved:    2024/01/28           #
######################################

from src.common.load_file import load_file
from hashlib import md5

year, day = 2015, 4

from multiprocessing import Process, Queue, cpu_count

STEP = cpu_count() - 1


def do_job(prefix: str, start: int, target: str, zeros: int, result: Queue):
    while md5((prefix + str(start)).encode()).hexdigest()[:zeros] != target:
        start += STEP
    result.put(start)
    return True


def get_number(prefix, zeros: int):
    processes: list[Process] = []
    result = Queue()
    target = "0" * zeros

    # creating processes
    for start in range(STEP):
        p = Process(target=do_job, args=(prefix, start, target, zeros, result))
        processes.append(p)

    for p in processes:
        p.start()

    number = result.get()

    for p in processes:
        p.terminate()

    return number


def run() -> None:
    input: list[str] = load_file(year, day)
    result = get_number(input[0].strip(), 5)

    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
