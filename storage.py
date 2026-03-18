import json

FILE = "seats.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {i: "Available" for i in range(1, 51)}

def save_data(seats):
    with open(FILE, "w") as f:
        json.dump(seats, f)