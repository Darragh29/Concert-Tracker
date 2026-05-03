import argparse
import api

def mock_save():
    print('saving...')

def mock_favourites():
    print('favourites...')

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# Creates subparser to parse search results
search = subparsers.add_parser('search')
search.add_argument('--artist', type=str, required=True)
search.add_argument('--city', type=str, required=True)
search.set_defaults(func=api.get_concert)

# Creates subparsers for saving to favourites and printing favourites
save = subparsers.add_parser('save')
save.set_defaults(func=mock_save)
favourites = subparsers.add_parser('favourites')
favourites.set_defaults(func=mock_favourites)

search_result = parser.parse_args()

search_result.func(search_result)
