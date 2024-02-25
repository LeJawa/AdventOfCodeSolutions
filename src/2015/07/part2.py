######################################
# Solution for part 2 of day 07/2015 #
#                                    #
#  Started:     2024/01/28           #
#  Finished:    2024/02/25           #
######################################

from src.common.load_file import load_file
from src.common.function_import import import_function
import copy

year, day = 2015, 7
input: list[str] = load_file(year, day)

def run() -> None:
    propagate_wires = import_function(2015,7,1, "propagate_wires")
    initialize_wiring = import_function(2015,7,1, "initialize_wiring")
    
    connexions, gates, entry_gates = initialize_wiring()
        
    original_gates = copy.deepcopy(gates)    
    next_gates = copy.deepcopy(entry_gates)
        
    result = propagate_wires(connexions, gates, next_gates)
    
    
    for index, (in1, gate, in2, out) in enumerate(entry_gates):
        if out == "b":
            entry_gates[index][0] = result
            entry_gates[index][2] = None
        
    result = propagate_wires(connexions, original_gates, entry_gates)    
    
    return str(result)

if __name__ == "__main__":
    result = run()
    print(f"Part 2 day {day} - {year}\nResult: {result}\n")
