import json

def save_last_search(data):
    with open('data/last_search.json', 'w') as f:
        json.dump(data,f)


def clear_last_search():
    with open('data/last_search.json', 'w') as f:
        json.dump([],f)