import sys
import os
sys.path.append(os.path.abspath('./day3'))
from day_03_01 import (
    make_string_array,
    find_numbers_in_row
)

def all_numbers(data) : 
    array = make_string_array(data)
    N = len(array)
    M = len(array[0])
    numbers = {(i,j) : v 
    for i in range(len(array))
    for j,v in find_numbers_in_row(i).items()}
    return numbers, N, M, array
def all_numbers_near_star(data) : 
    numbers, N, M, array = all_numbers(data)
    out = {} 
    for k,v in numbers.items() : 
        row_num = k[0]
        candidate_number = int("".join(v['numbers']))
        start, stop = v['start'], v['stop']
        start_row = row_num - 1 if row_num >= 1 else row_num
        end_row = row_num + 1 if row_num < N else row_num
        rows_iterable = range(start_row, end_row+1)
        start_column = start - 1 if start > 0 else start
        stop_column = stop + 1 if stop < M else stop
        cols_iterable = range(start_column, stop_column+1)
        for i in rows_iterable : 
            for j in cols_iterable : 
                if (i == row_num) & (j >= start) & (j <= stop) : 
                    continue
                elif i < N and j < M :  
                    try : 
                        if array[i][j] == '*' : 
                            out[k] = {'number':candidate_number,'star_place':(i,j)}
                    except : 
                        raise Exception(f"failed at {i},{j}")
                else : 
                    pass
    return out

# # new approach
# https://imgur.com/a/y4U7TDo
def search_grid(data) : 
    array = make_string_array(data)
    N = len(array)
    M = len(array[0])
    near_star = all_numbers_near_star(data)
    out = [(v['number'],v['star_place']) for v in near_star.values()]
    all_numbers = [x[0] for x in out]
    spaces = [x[1] for x in out]
    numbers = []
    for i, s in enumerate(spaces) : 
        if spaces.count(s) == 2 : 
            more = [x[0] for x in out if x[1] == s]
            assert len(more) == 2
            numbers.append(more[0] * more[1])
    return int(sum(numbers) / 2)

def main() : 
    directory = os.path.abspath('./day3')
    data_file = os.path.join(directory,"day_3_data.txt")
    with open(data_file, "r") as f : 
        data = f.read()
    print(search_grid(data))

if __name__ == "__main__" : 
    main()
