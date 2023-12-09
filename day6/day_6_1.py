import sys
import os
import re
folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(folder)
sys.path.append(os.path.dirname(folder))
from utils import load_data

def boat_charge(charge_ms, total_time) : 
    move_time = total_time - charge_ms
    speed = charge_ms
    distance = speed * move_time
    return distance

def how_many(time, distance) : 
    return sum(
        [
            1 for t in range(time) 
            if boat_charge(t, time) > distance
        ]
    )

def get_data(path) : 
    data = load_data(path)
    data = re.sub("\s{2,}"," ",data).split("\n")
    times = [int(x) for x in data[0].split(" ")[1:]]
    distances = [int(x) for x in data[1].split(" ")[1:]]
    return times, distances


def main() : 
    times, distances = get_data("day6/day_6_data.txt")
    out = 1
    for t, d in zip(times, distances) : 
        out *= how_many(t, d)
    print(out)

if __name__ == "__main__" : 
    main()
