import re
import sys
import os
from functools import reduce
folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(folder)
sys.path.append(os.path.dirname(folder))
from utils import load_data

def make_mapper(row) : 
    dest_start, orig_start, steps = [int(x)
    for x in row.strip().split(' ')]
    mapper = {orig_start + i : dest_start + i for i in range(steps)}
    return mapper

def split_data(data) : 
    splitted = data.split("\n\n")
    return splitted

def parse_rows(rows) : 
    rows_list = re.sub("[a-zA-Z\-:]","",rows).strip().split("\n")
    dict_join = lambda x, y : {**x, **y}
    mapper = reduce(dict_join,(make_mapper(r) for r in rows_list))
    return mapper

def parse_seeds(seeds) : 
    out = [int(x) 
    for x in re.sub("[a-zA-Z\-:]","",seeds).strip().split(" ")]
    return out


def dict_lookup(rows, value) : 
    rows_list = re.sub("[a-zA-Z\-:]","",rows).strip().split("\n")
    for r in rows_list : 
        dest, start, step = [int(x) for x in r.strip().split(' ')]
        if value >= start and value < start + step : 
            increment = value - start
            return dest + increment
        else : 
            continue
    return value

def make_steps(seeds_str, *args) : 
    seeds = parse_seeds(seeds_str)
    paths = [seeds]
    for a in args : 
        last = paths[-1]
        adds = [dict_lookup(a,l) for l in last]
        paths.append(adds)
    return paths

def main() : 
    data = load_data("day5/day_5_data.txt")
    splits = split_data(data)
    seeds, maps = splits[0], splits[1:]
    steps = make_steps(seeds, *maps)
    print(min(steps[-1]))

if __name__ == "__main__" : 
    main()