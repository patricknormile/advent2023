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
data = parse_data("day10/day10_data.txt")
walk(data, "_2")