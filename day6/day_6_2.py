import sys
import os
import re
folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(folder)
sys.path.append(os.path.dirname(folder))
from utils import load_data

from day_6_1 import (
    how_many,
    boat_charge,
    get_data
)

def main() : 
    times, distances = get_data("day6/day_6_data.txt")
    time = int("".join(str(x) for x in times))
    distance = int("".join(str(x) for x in distances))
    print(how_many(time, distance))

if __name__ == "__main__" : 
    main()
