import sys
import os
import re
folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(folder)
sys.path.append(os.path.dirname(folder))
from utils import load_data


def get_all_hands(path) : 
    data = load_data(path)
    hands_and_bids = [x.split(" ") for x in data.split("\n")]
    hands = [x[0] for x in hands_and_bids]
    bids = [int(x[1]) for x in hands_and_bids]
    return hands, bids

def determine_hand(hand) : 
    list_hand = list(hand)
    unique = set(list_hand)
    counts = [list_hand.count(x) for x in list_hand]
    if len(unique) == 5 : 
        # high card
        return 1
    if len(unique) == 4 : 
        # pair
        return 2
    if len(unique) == 3 and max(counts) < 3 :
        # two pair 
        return 3
    if len(unique) == 3 and max(counts) == 3 : 
        return 4
    if len(unique) == 2 and max(counts) < 4 :
        # full house
        return 5
    if len(unique) == 2 and max(counts) == 4 :
        # 4 of a kind
        return 6
    if len(unique) == 1 : 
        # 5 of a kind
        return 7

def rank(card, mapping) : 
    return mapping[card]


def is_greater(hand_1, hand_2, mapping) : 
    hand_1_l, hand_2_l = list(hand_1), list(hand_2)
    for h1, h2 in zip(hand_1_l, hand_2_l) : 
        r1, r2 = rank(h1, mapping), rank(h2, mapping)
        if r1 == r2 : 
            continue
        if r1 < r2 : 
            return False
        if r1 > r2 : 
            return True


def find_place(hand, bid, hands, bids, mapping) : 
    if len(hands) == 0 : 
        return [hand], [bid]
    elif len(hands) == 1 : 
        if is_greater(hand, hands[0], mapping) : 
            return hands + [hand], bids + [bid]
        else : 
            return [hand] + hands, [bid] + bids
    else : 
        for i, h in enumerate(hands) : 
            if is_greater(hand, h, mapping) : 
                continue
            else : 
                break
    if i + 1 == len(hands) : 
        out_hands = hands + [hand]
        out_bids = bids + [bid]
    elif i == 0 : 
        out_hands = [hand] + hands
        out_bids = [bid] + bids
    else :
        out_hands = hands[:i] + [hand] + hands[i:]
        out_bids = bids[:i] + [bid] + bids[i:]
    return out_hands, out_bids

def make_it_happen(hands, bids, mapping) : 
    data_store = dict(zip(range(1,8), [[[],[]]]*7))
    for h, b in zip(hands, bids) : 
        key = determine_hand(h)
        compare_hands = data_store[key][0]
        compare_bids = data_store[key][1]
        new_hands, new_bids = find_place(
            h, b, compare_hands, compare_bids, mapping
            )
        data_store[key] = [new_hands, new_bids]
    out_hands, out_bids = [], []
    for k , v in data_store.items() : 
        out_hands += v[0]
        out_bids += v[1]
    product = lambda x, y : x * y
    ranks = [*range(1,len(out_hands)+1)]
    out = sum((product(x, y) for x, y in zip(ranks, out_bids)))
    for h, b in zip(out_hands, out_bids) : 
        print(h, b)
    return out 

def main() : 
    order = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    mapping = dict(zip(order, range(len(order))))
    hands, bids = get_all_hands("day7/day_7_test_data_2.txt")
    print(make_it_happen(hands, bids, mapping))
    print(find_place("2345A",1, [],[], mapping))
    print(find_place("2345J",3, ["2345A"],[1], mapping))
    print(find_place("J345A", 2, ['2345J', '2345A'], [3, 1], mapping))
    print(find_place("T3T3J",17, [],[], mapping))
    print(find_place("KK677",7, ['T3T3J'], [17], mapping))
    print(find_place("KTJJT",34, ['T3T3J', 'KK677'], [17, 7], mapping))

if __name__ == "__main__" : 
    main()
    
