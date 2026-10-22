import os
import bs4
import requests
from dotenv import load_dotenv

load_dotenv()

user_year = str(input("What year would you like to travel to? Type the date in this format YYYY-MM-DD: "))
url = "https://appbrewery.github.io/bakeboard-hot-100/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(f"{url}{user_year}/", headers=headers)

soup = bs4.BeautifulSoup(response.text, "html.parser")

get_list = soup.find_all("h3", class_="chart-entry__title")
get_list = [tag.get_text(strip=True) for tag in get_list]

import ytmusicapi

raw_headers = f"""
Host: music.youtube.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:158.0) Gecko/20100101 Firefox/158.0
Accept: */*
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br, zstd
Content-Type: application/json
Content-Length: 2159
Referer: https://music.youtube.com/
Content-Encoding: gzip
X-Goog-Visitor-Id: CgtHX2kxQ1hzcHA0NCiOjejWBjIKCgJJThIEGgAgVmLCAgq_AkN1d0JDQVVTbmdFQjhRWnVaa2pFQ2t5azE0MkI4TmNvdlJlSUotRUFDa2JtWm9wV09WaHZWZ0cwaWtkaHFXQlM2a19leDUzSnlyWl9WV0lnc3N5VVFIamQyZ2hQV0RZM2pMYzVaT1pQbEp2OERYX0FXc2QzeDh6WGlnR0xNcUZWTmxITkZma3lGWDZHUkhjQy0zSWR1alZTS1dUUlVqUkJhNFJKa1dpRVFEZk1Cc2NqdzZGZzhuY1ZjcTdmZUphZEl1d3p1WVM4Q3JWdjQ2cUpjck42clRHNzN1R1N0Q2dGTWtVQjNxbWRUd0dNUDVVZ3NsUzRRbVdTUXhXTFR2bU5FZmZndGRYWkRuN2lRY3NuT0NEOG5WdVo2bTZwMWdJTUI3OGcyR2E5dUZFN2gtTXd1NWx1TWVrQjhrY1VKZ2M%3D
X-Youtube-Bootstrap-Logged-In: true
X-Youtube-Client-Name: 67
X-Youtube-Client-Version: 1.20261020.10.00
X-Goog-AuthUser: 0
X-Origin: https://music.youtube.com
Origin: https://music.youtube.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: same-origin
Sec-Fetch-Site: same-origin
Authorization: {os.getenv("AUTH")}
Connection: keep-alive
Alt-Used: music.youtube.com
Cookie: {os.getenv("COOKIE")}
Priority: u=4
TE: trailers
"""

ytmusicapi.setup(filepath="browser.json", headers_raw=raw_headers)
print("browser.json has been created successfully!")

yt = ytmusicapi.YTMusic("browser.json")
playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

playlist_id = yt.create_playlist(
    title="2026-03-14 Billboard 100",
    privacy_status="PRIVATE",
    description="Python Projects - Musical Time Machine",
)
print(f"Playlist created successfully! ID: {playlist_id}")

for song in get_list:
  try:
    search_results = yt.search(song, filter="songs")

    if search_results:
      video_id = search_results[0]["videoId"]

      yt.add_playlist_items(playlist_id, [video_id])
      print(f"Successfully added: {song}")
    else:
      print(f"Could not find a match for: {song}")

  except Exception as e:
    print(f"Error adding {song}: {e}")

print("All done! Check your YouTube Music library.")
