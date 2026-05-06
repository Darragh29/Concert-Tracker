# 🎵 Concert Tracker

A command line tool to search for upcoming concerts by artist and city, save your favourites, and view them anytime — without trawling Ticketmaster.

Built with Python using the Ticketmaster Discovery API.

---

## Features

- Search for upcoming concerts by artist and city
- Save specific events or entire search results to your favourites
- View all saved favourites sorted by date
- Clean, readable output in the terminal

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/concert-tracker.git
cd concert-tracker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Ticketmaster API key

Create a `.env` file in the root of the project:

```
TICKETMASTER_API_KEY=your_api_key_here
```

Get a free API key at [developer.ticketmaster.com](https://developer.ticketmaster.com)


---

## Usage

All commands are run from the `src/` directory:

```bash
cd src
```

### Search for concerts

```bash
python3 main.py search --artist "Metallica" --city "Dublin"
```

Returns a numbered list of upcoming events matching the artist and city.

### Save a specific event

```bash
python3 main.py save --event 2
```

Saves event number 2 from your last search to your favourites.

### Save all results from last search

```bash
python3 main.py save
```

Saves every result from your last search to favourites.

### View your favourites

```bash
python3 main.py fav
```

Displays all saved concerts sorted by date.

---

## Project Structure

```
concert-tracker/
│
├── src/
│   ├── main.py       # Entry point, handles CLI commands
│   ├── api.py        # Ticketmaster API calls
│   ├── storage.py    # Reading and writing JSON files
│   └── display.py    # Formatting and printing results
│
├── data/
│   ├── last_search.json   # Temporary search results
│   └── favourites.json    # Saved concerts
│
├── .env                   # API key (never committed)
├── .env.example           # Safe template for API key
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Example Output

```
1.
Artist: Metallica: M72 World Tour
City: Dublin
Venue: Aviva Stadium
Date: 19 June 2026
Buy Tickets Here: https://www.ticketmaster.ie/...

──────────────────────────────
2.
Artist: Metallica: M72 World Tour
City: Dublin
Venue: Aviva Stadium
Date: 21 June 2026
Buy Tickets Here: https://www.ticketmaster.ie/...
```

---

## Built With

- Python 3
- [Requests](https://docs.python-requests.org/) — HTTP requests
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Environment variable management
- [Ticketmaster Discovery API](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/)
