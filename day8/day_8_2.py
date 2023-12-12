import sys
import os
import re
from math import gcd, lcm
folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(folder)
sys.path.append(os.path.dirname(folder))
from utils import load_data
from day_8_1 import parse_data

def find_starting_a(mapper) : 
    return [k for k in mapper.keys() if k.endswith("A")]

def ends_with_z(string) : 
    if string.endswith("Z") : 
        return True
    else : 
        return False
def last_was_z(l) : 
    return ends_with_z(l[-1])

def follow_instructions(instructions, mapper) : 
    starting_a = find_starting_a(mapper)
    tracking = {a : a for a in starting_a}
    multiples = {a : 0 for a in starting_a}
    i = 1
    while i < 999999999 : 
        for step in instructions : 
            index = 0 if step == "L" else 1
            for ghost in tracking : 
                k = tracking[ghost]
                values = mapper[k]
                v = values[index]
                tracking[ghost] = v
                if ends_with_z(v) and multiples[ghost] == 0 : 
                    multiples[ghost] = i
            i += 1
            # if all(map(ends_with_z, tracking.values())) : 
            #     return i
            if all(map(lambda x : x > 0, multiples.values())) : 
                return multiples
    raise Exception(f"could not complete after {i}")
    
def lcm_of_ghosts(ghosts) : 
    numbers = [*ghosts.values()]
    return lcm(*numbers)

def main() : 
    instructions, mapper = parse_data("day8/day_8_data.txt")
    ghosts = follow_instructions(instructions, mapper)
    print(lcm_of_ghosts(ghosts))

if __name__ == "__main__" : 
    main()
