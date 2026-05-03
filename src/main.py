import argparse
import api
import storage

def mock_save():
    print('saving...')

def mock_favourites():
    print('favourites...')

def handle_search(args):
    results = api.get_concert(args)
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
save.set_defaults(func=mock_save)
favourites = subparsers.add_parser('favourites')
favourites.set_defaults(func=mock_favourites)

search_result = parser.parse_args()

search_result.func(search_result)