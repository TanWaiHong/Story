import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from selenium import webdriver

scopes = "playlist-modify-private"
CLIENT_ID = "1e7cbfc381d94792be7048f96b7576a2"
CLIENT_SECRET = "5134d39b1c8f459cb8a67a38008c44c4"
language = input("what language of song would you like?(CN/EN): ")
travel_date = input("Which year do you want to travel to ? "
                    "Type the data in this format YYYY-MM-DD: ")

if language == "CN":
    URL = f"https://kma.kkbox.com/charts/daily/song?cate=297&date={travel_date}&lang=tc&terr=tw"
    item = "charts-list-song"
    chrome_driver_path = "C:/Users/User/Desktop/coding/store/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(URL)
    song_raw_data = driver.find_elements_by_class_name(item)
    song_data = [song.text for song in song_raw_data if song.text != ""]
    driver.quit()

else:
    URL = f"https://www.billboard.com/charts/hot-100/{travel_date}"

    response = requests.get(URL)
    website_html = response.text

    soup = BeautifulSoup(website_html, "html.parser")
    song_raw_data = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
    song_data = [song.getText() for song in song_raw_data]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scopes,
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()['id']
song_uris = list()
year = travel_date.split("-")[0]

for song in song_data:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

play_list = sp.user_playlist_create(
    user=user_id,
    name=f"{travel_date} {language} song",
    public=False
)


sp.playlist_add_items(
    playlist_id=play_list["id"],
    items=song_uris
)
