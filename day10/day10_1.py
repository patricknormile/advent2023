import sys
import os
folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(folder)
sys.path.append(os.path.dirname(folder))
from utils import load_data

def parse_data(path) : 
    data = load_data(path) 
    rows = data.split("\n")
    matrix = [list(x) for x in rows]
    return matrix

def first_step(row,column, data) : 
    possible = ["|","-","L","J","7","F"]
    out = []
    if data[row-1][column] in ["|","7","F"] : 
        out.append((row-1, column))
    if data[row][column -1] in ["-","L","F"] : 
        out.append((row, column-1))
    if data[row][column + 1] in ["-","J","7"] : 
        out.append((row, column + 1))
    if data[row + 1][column] in ["|","L","J"] : 
        out.append((row + 1, column))
    assert len(out) == 2
    return out[0], out[1]

def find_s(data) : 
    for i, r in enumerate(data) : 
        for j, c in enumerate(r) : 
            if data[i][j] == "S" :
                return i, j
    raise Exception("didn't find")

def step(row, column, previous_row, previous_column, data) : 
    pipe = data[row][column] 
    if pipe == "|" : 
        if row == previous_row - 1 : 
            return row - 1, column
        elif row == previous_row + 1 : 
            return row + 1, column
    if pipe == "-" : 
        if column == previous_column - 1 : 
            return row, column - 1
        elif column == previous_column + 1 : 
            return row, column + 1
    if pipe == "L" : 
        if row == previous_row + 1 : 
            return row, column + 1
        elif column == previous_column - 1 : 
            return row - 1, column
    if pipe == "J" : 
        if column == previous_column + 1 : 
            return row - 1, column
        elif row == previous_row + 1 : 
            return row, column - 1 
    if pipe == "7" : 
        if column == previous_column + 1 : 
            return row + 1, column
        elif row == previous_row - 1 : 
            return row, column - 1
    if pipe == "F" : 
        if row == previous_row - 1 : 
            return row, column + 1
        elif column == previous_column - 1 : 
            return row + 1, column

def make_data_string(data) : 
    data = [[str(y) for y in x] for x in data]
    string = "\n".join(["".join(x) for x in data])
    return string

def walk(data, suffix="", fill_value="0") :
    start_r, start_c = find_s(data)
    path_0, path_1 = first_step(start_r, start_c, data)
    current_path_0_r = path_0[0]
    current_path_0_c = path_0[1]
    prev_path_0_r = start_r
    prev_path_0_c = start_c
    current_path_1_r = path_1[0]
    current_path_1_c = path_1[1]
    prev_path_1_r = start_r
    prev_path_1_c = start_c
    i = 1 
    while True : 
        try : 
            next_path_0_r, next_path_0_c = step(
                current_path_0_r,
                current_path_0_c,
                prev_path_0_r,
                prev_path_0_c,
                data
            )
        except Exception as e : 
            v = data[current_path_0_r][current_path_0_c]
            raise Exception(str(*e.args) +" "+ str(i)+" "+str(v)+" path 0")
        try : 
            next_path_1_r, next_path_1_c = step(
                current_path_1_r,
                current_path_1_c,
                prev_path_1_r,
                prev_path_1_c,
                data
            )
        except Exception as e : 
            v = data[current_path_1_r][current_path_1_c]
            raise Exception(str(*e.args) +" "+ str(i)+" "+str(v)+" path 1")
        i += 1
        if i > 2 : 
            data[prev_path_0_r][prev_path_0_c] = fill_value
            data[prev_path_1_r][prev_path_1_c] = fill_value
        if (
            (next_path_0_r == next_path_1_r) & 
            (next_path_0_c == next_path_1_c)
            ): 
            with open(f"day10/output{suffix}.txt", 'w') as _f_ : 
                string = make_data_string(data)
                _f_.write(string)
            break
        else : 
            prev_path_0_r = current_path_0_r
            prev_path_0_c = current_path_0_c
            prev_path_1_r = current_path_1_r
            prev_path_1_c = current_path_1_c
            current_path_0_r = next_path_0_r
            current_path_0_c = next_path_0_c
            current_path_1_r = next_path_1_r
            current_path_1_c = next_path_1_c
        if i > 9999999 : 
            raise Exception("too many iterations")
    return i



def main() : 

    data = parse_data("day10/day10_data.txt")
    print(walk(data))

if __name__ == "__main__" : 
    main()
