import sys
import os
folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(folder)
sys.path.append(os.path.dirname(folder))
from utils import load_data

from day9_1 import (
    difference,
    get_diff_sequence,
    parse_data,
)

def get_pre_prediction(row) : 
    diff_sequences = get_diff_sequence(row) 
    for i,diffs in list(enumerate(diff_sequences[1:], 1))[::-1] :
        add = diff_sequences[i][0]
        # diff_sequences[i] = [add] + diffs
        next = diff_sequences[i - 1][0]
        diff_sequences[i - 1] = [next - add] + diff_sequences[i - 1]
    return diff_sequences[0][0]

def get_sum_pre(data) : 
    iterations = [get_pre_prediction(d) for d in data]
    return sum(iterations)

def main() : 
    data = parse_data("day9/day9_data.txt")
    print(get_sum_pre(data))

if __name__ == "__main__" : 
    main()
