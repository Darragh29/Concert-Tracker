import argparse
import api
import storage
import display
import json

def save_favourites(args):
    last_search = storage.get_last_search()

    if args.event is not None:
        storage.save_favourites([last_search[args.event - 1]])
    else:
        storage.save_favourites(last_search)

def load_favourites(args):
    storage.load_favourites()

def handle_search(args):
    results = api.get_concert(args)
    display.display_concert(results)
    storage.clear_last_search()
    storage.save_last_search(results)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# Creates subparser to parse search results
search = subparsers.add_parser('search')
search.add_argument('--artist', type=str, required=True)
search.add_argument('--city', type=str, required=True)
search.set_defaults(func=handle_search)

# Creates subparsers for saving to favourites and printing favourites
save = subparsers.add_parser('save')
save.add_argument('--event', type=int, required=False)
save.set_defaults(func=save_favourites)

favourites = subparsers.add_parser('fav')
favourites.set_defaults(func=load_favourites)

search_result = parser.parse_args()

search_result.func(search_result)