import json

def sold_bottle_count():
    with open("bottle_count.json", "r") as file:
        data = json.load(file)
        return int(data['count'])