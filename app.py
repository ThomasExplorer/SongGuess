import csv
from random import random

songs = []
artists = []

with open('top200songs.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # skip past field names
    for line in csv_reader:
        songs.append(line[0])
        artists.append(line[1])

count = 0
print('Thomas')
print("SONGS")
for song in songs:
    count += 1
    print(count, song)

print("ARTISTS")
for artist in artists:
    print(artist)

random_song_number = int(random()*len(songs))
print(random_song_number)

random_song = songs[random_song_number]
print(random_song)

artist = artists[random_song_number]
print('by', artist)

words_of_title = random_song.split()
for word in words_of_title:
    print(word[0])












