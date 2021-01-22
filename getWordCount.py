import json

with open("allFemaleSongs.json", "r") as of:
    data = json.load(of)



sum = 0
numSongs = 0

for key in data:
    songs = data.get(key)
    for song in songs:
        sum += len(song.split())
        numSongs += 1

print(sum)
print(numSongs)