import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# Creates subparser to parse search results
search = subparsers.add_parser('search')
search.add_argument('--artist', type=str, required=True)
search.add_argument('--city', type=str, required=True)

# Creates subparsers for saving to favourites and printing favourites
save = subparsers.add_parser('save')
favourites = subparsers.add_parser('favourites')

search_result = parser.parse_args()

print(search_result.artist)