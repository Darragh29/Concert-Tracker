import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('KEY')

def get_concert(args):
    city = args.city
    artist = args.artist
    url = f'https://app.ticketmaster.com/discovery/v2/events?apikey={api_key}&keyword={artist}&locale=*&city={city}'

    response = requests.get(url)
    data = response.json()

    formatted_data = data['_embedded']['events']
    final_data = []

    for event in formatted_data:
        data_json = {'name':event['name'],
                     'venue':event['_embedded']['venues'][0]['name'],
                     'city':event['_embedded']['venues'][0]['city']['name'],
                     'date':event['dates']['start']['localDate'],
                     'link':event['url']}

        final_data.append(data_json)

    return final_data

