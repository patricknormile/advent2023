import sys
import os
import re
folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(folder)
sys.path.append(os.path.dirname(folder))
from utils import load_data

def make_row_kv(row) : 
    k, v = row.split(" = ")
    v = re.sub(r"[\(\)]","",v)
    vs = tuple(v.split(", "))
    return k, vs

def parse_data(path) : 
    data = load_data(path)
    parts = data.split('\n\n')
    assert len(parts) == 2
    instructions = parts[0]
    maps = parts[1]
    mapper = {}
    for m in maps.split("\n") : 
        k, v = make_row_kv(m)
        mapper[k] = v
    return instructions, mapper

def follow_instructions(instructions, mapper) : 
    i = 0
    key = "AAA"
    while i < 1000000: 
        for step in instructions : 
            values = mapper[key]
            if step == "L" :
                v = values[0]
            elif step == "R" : 
                v = values[1]
            else : 
                raise ValueError("Not L or R")
            i += 1 
            if v == "ZZZ" : 
                return i
            else :
                key = v
    raise Exception(f"Did not complete after {i}")
        


def main() : 
    instructions, mapper = parse_data("day8/day_8_data.txt")
    print(len(instructions))
    print(follow_instructions(instructions, mapper))

if __name__ == "__main__" : 
    main()
