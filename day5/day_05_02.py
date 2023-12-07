import sys
import os
import re
folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(folder)
sys.path.append(os.path.dirname(folder))
from utils import load_data

from day_05_01 import (
    split_data,
    dict_lookup,
)
def parse_seeds(seeds) : 
    seedssteps = [int(x) 
    for x in re.sub("[a-zA-Z\-:]","",seeds).strip().split(" ")]
    n = len(seedssteps)
    for x in range(0, n, 2) : 
        for i in range(seedssteps[x+1]) : 
            yield seedssteps[x] + i

def get_shortest(seeds_str, *args) : #switch order, use generators
    seeds = parse_seeds(seeds_str)
    shortest = 99999999999
    for s in seeds : 
        path = [s]
        for a in args : 
            last = path[-1]
            adds = dict_lookup(a,last)
            path.append(adds)
        if path[-1] < shortest : 
            print(f"shortest at seed {s} value {path[-1]}")
            shortest = path[-1]
    return shortest

def main() : 
    data = load_data("day5/day_5_data.txt")
    splits = split_data(data)
    seeds, maps = splits[0], splits[1:]
    print(get_shortest(seeds, *maps))
    

if __name__ == "__main__" : 
    main()