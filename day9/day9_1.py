import sys
import os
folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(folder)
sys.path.append(os.path.dirname(folder))
from utils import load_data

def difference(array) : 
    return [array[i+1] - array[i] for i in range(len(array)-1)]

def get_diff_sequence(array) : 
    differences = [array]
    i = 0
    while not all(map(lambda x : x==0, differences[-1])) : 
        diff_seq = difference(differences[-1])
        differences.append(diff_seq)
        i += 1
        if i > 1000 : 
            raise Excpetion("over loop")
    return differences

def get_prediction(row) : 
    diff_sequences = get_diff_sequence(row) 
    n_steps = len(diff_sequences)
    for i,diffs in list(enumerate(diff_sequences[1:], 1))[::-1] :
        add = diffs[-1]
        next = diff_sequences[i - 1][-1]
        diff_sequences[i - 1].append(add + next)
    return diff_sequences[0][-1]
    

def parse_data(path) : 
    data = load_data(path)
    rows = data.split("\n")
    ints = [[int(j) for j in x.split(" ")] for x in rows]
    return ints

def get_sum(data) : 
    iterations = [get_prediction(d) for d in data]
    return sum(iterations)
        

def main() : 
    data = parse_data("day9/day9_data.txt")
    print(get_sum(data))

if __name__ == "__main__" : 
    main()
