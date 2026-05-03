import json

def save_last_search(data):
    with open('data/last_search.json', 'w') as f:
        json.dump(data,f)

def clear_last_search():
    with open('data/last_search.json', 'w') as f:
        json.dump([],f)

def get_last_search():
    with open('data/last_search.json', 'r') as f:
        data = json.load(f)
        return data

def save_favourites():
    last_search = {}
    with open('data/last_search.json', 'r') as f:
        last_search = json.load(f)

    with open('data/favourites.json', 'r') as favourites:
        existing_favourites = json.load(favourites)
        existing_favourites.append(last_search)

    with open('data/favourites.json', 'w') as new_favourites:
        json.dump(existing_favourites, new_favourites)
