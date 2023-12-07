import sys
import os
import re
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from day_04_01 import (
    load_data,
    data_rows,
    winning_numbers_and_yours
)

def score(row) : 
    winning, yours = winning_numbers_and_yours(row)
    winning_set, yours_set = set(winning), set(yours)
    win_size = len(winning_set & yours_set)
    return win_size
def copies(rows) : 
    N = len(rows)
    initial = [0]*N
    out = dict(zip(range(N),initial))
    for i, item in enumerate(rows) : 
        out[i] += 1
        scr = score(item)
        for k in range(out[i]) : 
            if scr > 0 : 
                for j in range(1, scr+1) :
                    out[i + j] += 1
    return out

def main() : 
    data = load_data("day_4_data.txt")
    rows = data_rows(data)
    games = copies(rows)
    print(sum(games.values()))
    
    

if __name__ == "__main__" : 
    main()
    