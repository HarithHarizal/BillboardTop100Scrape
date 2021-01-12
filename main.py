import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.billboard.com/charts/hot-100")
soup = BeautifulSoup(page.content, "html.parser")

#Classes
song_rank = soup.find_all(class_="chart-element__rank__number")
song_names = soup.find_all(class_="chart-element__information__song")
artist_names = soup.find_all(class_="chart-element__information__artist")

hot_100 = []

def print_top_100_song_list(song_info):
  print(f'Rank: {song_info["rank"]}')
  print(f'Artist: {song_info["artist"]}')
  print(f'Song: {song_info["song"]}')
  print('')

for index, song in enumerate(song_names):
  song_info = {
    "artist": artist_names[index].get_text().strip(),
    "song": song_names[index].get_text().strip(),
    "rank": index + 1
    }
  index += 1
  hot_100.append(song_info)

for song in hot_100:
  print_top_100_song_list(song)
