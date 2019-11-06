import csv
from random import random

songs = []
artists = []

total_songs = 0
total_duplicates = 0
count = 0

with open('newtop200songs.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # skip past field names
    for line in csv_reader:
        count += 1
        print(count)
        if line[0] not in songs:
            songs.append(line[0])
            artists.append(line[1])
            total_songs += 1
            print('added song - ' + line[0])
        else:
            print('found duplicate - ' + line[0])
            total_duplicates += 1

count = 0
print("SONGS")
for song in songs:
    count += 1
    print(count, song)

print("ARTISTS")
for artist in artists:
    print(artist)

print('count', count)
print('len(songs)', len(songs))

random_song_number = int(random()*len(songs))
print(random_song_number)

artist = artists[random_song_number]
print('by', artist)

random_song = songs[random_song_number]
words_of_title = random_song.split()
for word in words_of_title:
    print(word[0])

input()
print(random_song)











