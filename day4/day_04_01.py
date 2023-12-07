import os
import re
def load_data() : 
    directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, "day_4_data.txt")
    with open(file_path, "r") as f_ : 
        data = f_.read()
    return data

def data_rows(data) : 
    return data.split("\n")

def winning_numbers_and_yours(row) : 
    remove_card = re.sub("Card\s+\d+:","", row)
    sides = remove_card.split("|")
    regex = r"\d{1,2}"
    winning = re.findall(regex, sides[0])
    yours = re.findall(regex, sides[1])
    winning = [int(x.strip()) for x in winning]
    yours = [int(x.strip()) for x in yours]
    return winning, yours

def score(row) : 
    winning, yours = winning_numbers_and_yours(row)
    winning_set, yours_set = set(winning), set(yours)
    win_size = len(winning_set & yours_set)
    if win_size == 0 : 
        return 0
    else : 
        return 2 ** (win_size - 1)




def main() : 
    data = load_data()
    rows = data_rows(data)
    scores = [score(row) for row in rows]
    print( sum(scores))
if __name__ == "__main__" : 
    main()