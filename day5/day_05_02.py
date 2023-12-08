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
            if i % 5000 == 0 : 
                yield seedssteps[x] + i

def get_shortest(seeds_str, *args) : 
    seeds = parse_seeds(seeds_str)
    shortest = 99999999999
    for s in seeds : # do range insntead ? 
        path = [s]
        for a in args : 
            last = path[-1]
            adds = dict_lookup(a,last) # parse out rows so faster
            path.append(adds)
        if path[-1] < shortest : 
            shortest = path[-1]
            seed = s
            print(f"at seed {s}, shortest value {shortest}")
    return seed, shortest

def down_from_shortest_seed(seed, shortest, *args) : 
    new_shortest = shortest 
    for i in range(5000) : 
        s = seed - i
        path = [s]
        for a in args : 
            last = path[-1]
            adds = dict_lookup(a, last)
            path.append(adds)
        if path[-1] < new_shortest : 
            new_shortest = path[-1]
            print(f"at seed {s}, shortest value {new_shortest}")
    return new_shortest

def main() : 
    data = load_data("day5/day_5_data.txt")
    splits = split_data(data)
    seeds, maps = splits[0], splits[1:]
    seed, short = get_shortest(seeds, *maps)
    shortest = down_from_shortest_seed(seed, short, *maps)
    print(shortest)
    

if __name__ == "__main__" : 
    main()