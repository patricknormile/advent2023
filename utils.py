import os

def load_data(file="day_4_data.txt") : 
    directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, file)
    with open(file_path, "r") as f_ : 
        data = f_.read()
    return data