from datetime import datetime
from time import strftime


def display_concert(concerts):
    for i,concert in enumerate(concerts,1):
        format_date = datetime.strptime(concert['date'],'%Y-%m-%d')
        date = format_date.strftime('%d %B %Y')
        print(f"{i}.\nArtist: {concert['name']}\nCity: {concert['city']}\nVenue: {concert['venue']}\nDate: {date}\nBuy Tickets Here: {concert['link']}\n\n")