import csv
from random import random
songs = []
artists = []
# name = input("Name: ")
# password = input("Password: ")
#
# if name != "Thomas" or password != "password":
#     print("Sorry you are not authorised or you have the password incorrect")
#     quit()
#
# if name == "Thomas" and password == "password":
#     print("Hello", name + ', welcome to the music quiz game!')

with open('playlist.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        if line[0] not in songs:
            songs.append(line[0])
            artists.append(line[1])

score = 0
round_no = 0

loop = True
while loop:
    round_no = round_no + 1
    random_song_number = int(random() * len(songs))
    random_song = songs[random_song_number]
    artist = artists[random_song_number]
    print('Round', round_no)
    print('Artist:', artist)
    words_of_title = random_song.split()
    for word in words_of_title:
        print(word[0])
    guess = input("Song Name: ")
    if guess == random_song:
        score = score + 1
        print('Correct! Your score is', score)
        print('Next song...')
        print('')
    if guess != random_song:
        print("Incorrect. Your score is", score)
        break

