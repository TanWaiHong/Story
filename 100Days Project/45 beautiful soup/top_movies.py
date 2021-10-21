import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
movies_raw_data = soup.find_all(name="a", target="_self")
data = [movies.getText() for movies in movies_raw_data ]
all_movies = [movies.replace("Read Empire's review of ", "") for movies in data if "Read Empire's review of " in movies]
print(all_movies[::-1])


