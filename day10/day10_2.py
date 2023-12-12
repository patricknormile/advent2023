import sys
import os
folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(folder)
sys.path.append(os.path.dirname(folder))
from utils import load_data
from day10_1 import (
    parse_data,
    first_step,
    find_s,
    step,
    make_data_string,
    walk
)

def scaline(data, data2, loop_char="o") : 
    points = 0
    
    for i,row in enumerate(data) : 
        in_region = False 
        last = "."
        for j,pixel in enumerate(row) : 
            part_of_loop = True if data2[i][j] == loop_char else False

            if pixel == "|" : 
                in_region = not in_region
                continue
            if not in_region and pixel == "F" and last in ('.',"F") : 
                last = "F"
                continue
            if not in_region and pixel == "L" and last == '.' : 
                last = "L"
                continue
            if not in_region and pixel in "7" and last == "F" : 
                last = "."
                continue
            if not in_region and pixel == "7" and last == "L" : 
                in_region = not in_region
                last = "."
                continue
            if not in_region and pixel == "J" and last == "F" : 
                in_region = not in_region
                last = "."
                continue
            if not in_region and pixel == "J" and last == "L" : 
                last = "."
                continue
            if in_region and pixel == "." : 
                points += 1
            if in_region and pixel == 0 : 
                pass
    return points

def main() : 
    data = parse_data("day10/day10_data.txt")
    walk(data, "_2", "o")
    data2 = parse_data("day10/output_2.txt")
    print(data2)
    print(scaline(data, data2))


if __name__ == "__main__" : 
    main()