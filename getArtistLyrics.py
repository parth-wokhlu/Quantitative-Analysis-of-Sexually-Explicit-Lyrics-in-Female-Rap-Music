import json

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config
import spotify
import lyricsgenius
import itunespy

genius = lyricsgenius.Genius(config.geniusToken)
# genius.artist_albums()

file = open("peee.txt", "r")
lines = file.readlines()
artists = []

for line in lines:
    line = line[0:len(line) - 1].strip()
    artists.append(line)
"""
for name in artists:
    try:
        artist = itunespy.search_artist(name)
        artistId = artist[0].artist_id
        albums = artist[0].get_albums()  # Get albums from the first result
        albumList = []
        for album in albums:
            if album.artist_id == artistId and album.collection_name.count("(Deluxe") == 0 and album.collection_name.count("Single") == 0 and album.collection_name.count("(Bonus") == 0:
                print(str(album.artist_id) + " || " + album.collection_name + " || " + album.artist_name)
                albumList.append(album.collection_name)
                with open("extrafemalesongs.json", "r") as of:
                    data = json.load(of)

                with open("extrafemalesongs.json", "w") as of:
                    data.update({artist[0].artist_name: albumList})
                    json_object = json.dumps(data, indent=4)
                    of.write(json_object)
    except:
        print(name + " DIDN'T WORK")
"""
with open("extrafemalesongs.json", "r") as of:
    data = json.load(of)

lyrics = []


for name in data:
    albums = data.get(name)
    for album in albums:
        person = genius.search_albums(album + " " + name)
        try:
            tracks = genius.album_tracks(person.get("sections")[0].get("hits")[0].get("result").get("id"))
            for track in tracks.get("tracks"):
                title = track.get("song").get("title")
                try:
                    lyrics.append(genius.search_song(title=title, artist=name).lyrics)
                except:
                    pass
        except:
            pass

    with open("allFemaleSongs.json", "r") as of:
        d = json.load(of)

    with open("allFemaleSongs.json", "w") as of:
        d.update({name: lyrics})
        json_object = json.dumps(d, indent=4)
        of.write(json_object)

    lyrics = []