import sys
import os
import re
from math import gcd, lcm
folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(folder)
sys.path.append(os.path.dirname(folder))
from utils import load_data

def parse_data_to_list(path) : 
    data = load_data(path) 
    rows = data.split("\n")
    return rows

def parse_data_matrix(path) : 
    rows = parse_data_to_list(path) 
    matrix = [list(x) for x in rows]
    return matrix

def find_rows_all_space(data) : 
    ids = []
    for i,r in enumerate(data) : 
        if all(map(lambda x : x==".", r)) :
            ids.append(i)
    data_out = data
    for i in reversed(ids) :
        row = data[i]
        n = len(row)
        ads = "."*n
        data_out = data_out[:i] +[ads] + data_out[i:]
    return data_out

def find_columns_all_space(data) : 
    ids = []
    n = len(data[0])
    assert all(map(lambda x : len(x)==n, data))
    for i in range(n) : 
        id_vals = [r[i] for r in data]
        if all(map(lambda x : x==".", id_vals)) :
            ids.append(i)
    data_out = data
    for i in reversed(ids) : 
        for j in range(n) : 
            data_out[j] = data_out[j][:i] + "." + data_out[j][i:]
    return data_out

def expand_space(data) : 
    data = find_columns_all_space(data)
    data = find_rows_all_space(data)
    string = "\n".join(data)
    path = "day11/output_expand.txt"
    with open(path, "w") as _f_ : 
        _f_.write(string)
    data = parse_data_to_list(path)
    return data

def get_locations(matrix) : 
    k=0
    locations = {}
    for i, row in enumerate(matrix) : 
        for j, col in enumerate(row) : 
            if matrix[i][j] != "." : 
                locations[k] = (i, j)
                k+=1
    return locations

def taxicab_distance(x1, y1, x2, y2) : 
    return abs(x1 - x2) + abs(y1 - y2)

def get_shortest_distances(locs) : 
    short_distance = {}
    for k1,v1 in locs.items() : 
        short_distance[k1] = 99999999
        for k2, v2 in locs.items() : 
            if k2 == k1 : 
                continue
            dist = taxicab_distance(v1[0], v1[1], v2[0], v2[1])
            if dist < short_distance[k1] : 
                short_distance[k1] = dist
    return short_distance

def get_all_distances(locs) : 
    distance = {}
    for k1,v1 in locs.items() : 
        distance[k1] = []
        for k2, v2 in locs.items() : 
            if k2 == k1 : 
                continue
            dist = taxicab_distance(v1[0], v1[1], v2[0], v2[1])
            distance[k1].append(dist)
    return distance


def main() :
    data = parse_data_to_list("day11/day11_data.txt")
    _ = expand_space(data)
    matrix = parse_data_matrix("day11/output_expand.txt")
    locs = get_locations(matrix)
    dists = get_all_distances(locs)
    print(int(sum([sum(x) for x in dists.values()])/2))

if __name__ == "__main__" : 
    main()
