import requests

def get_concert(args):
    city = args.city
    artist = args.artist
    url = f'https://app.ticketmaster.com/discovery/v2/events?apikey=SWCQjZrFBSHfVXXaqjs8Wnt8vLHR8KXj&keyword={artist}&locale=*&city={city}'

