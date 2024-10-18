######################################
# Solution for part 1 of day 07/2015 #
#                                    #
#  Started:     2024/01/28           #
#  Finished:    2024/02/25           #
######################################

from src.common.load_file import load_file, load_test_file
from src.common.function_import import import_function
import re

year, day = 2015, 7
input: list[str] = load_file(year, day)
# input: list[str] = load_test_file(year, day)


def calculate_gate(gate_list: list[str]) -> int:
    if gate_list[0]:
        in1 = int(gate_list[0])
    if gate_list[1]:
        in2 = int(gate_list[1])

    gate = gate_list[2]
    if not gate:
        return in1

    if gate == "NOT":
        return ~in2
    if gate == "AND":
        return in1 & in2
    if gate == "OR":
        return in1 | in2
    if gate == "RSHIFT":
        return in1 >> in2
    # gate == "LSHIFT"
    return in1 << in2


def can_calculate_gate(gate_list) -> bool:
    try:
        if gate_list[0]:
            in1 = int(gate_list[0])
        if gate_list[1]:
            in2 = int(gate_list[1])
        return True
    except:
        return False


def propagate_wires(
    connexions: dict[str, list[int]],
    gates: list[list[str]],
    next_gates: list[list[str]],
) -> int:
    result = -1
    while len(next_gates) > 0:
        next = next_gates.pop()
        if not can_calculate_gate(next):
            continue
        result = calculate_gate(next)
        out = next[3]

        if out == "a":
            break

        if out not in connexions.keys():
            continue
        for index in connexions[out]:
            if gates[index][0] == out:
                gates[index][0] = str(result)
                if gates[index] not in next_gates:
                    next_gates.append(gates[index])
            if gates[index][1] == out:
                gates[index][1] = str(result)
                if gates[index] not in next_gates:
                    next_gates.append(gates[index])
    return result


def initialize_wiring():
    connexions: dict[str, list[int]] = {}
    gates: list[list[str, str, str, str]] = []
    pattern = r"^([a-z0-9]+)? ?(NOT|OR|AND|RSHIFT|LSHIFT)? ?([a-z0-9]+)? -> ([a-z]+)"

    entry_gates: list[list[str]] = []

    for line in input:
        in1, gate, in2, out = re.match(pattern, line).groups()

        gates.append([in1, in2, gate, out])
        if not in1 in connexions.keys():
            connexions[in1] = []
        connexions[in1].append(len(gates) - 1)
        if not in2 in connexions.keys():
            connexions[in2] = []
        connexions[in2].append(len(gates) - 1)

        if gate != None:
            continue
        entry_gates.append([in1, in2, gate, out])
    return connexions, gates, entry_gates


def run() -> None:
    connexions, gates, entry_gates = initialize_wiring()

    result = propagate_wires(connexions, gates, entry_gates)

    return str(result)


if __name__ == "__main__":
    result = run()
    print(f"Part 1 day {day} - {year}\nResult: {result}\n")
