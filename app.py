import csv
from random import random
songs = []
artists = []
name = input("Name: ")
password = input("Password: ")

if password != "password":
    print("Sorry you are not authorised or you have the password incorrect")
    quit()

if password == "password":
    print("Hello", name + ', welcome to the music quiz game!')

with open('playlist.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        if line[0] not in songs:
            songs.append(line[0])
            artists.append(line[1])

random_song_number = int(random() * len(songs))
random_song = songs[random_song_number]
artist = artists[random_song_number]

score = 0
round_no = 0
loop = 2

while loop == 2:
    random_song_number = int(random() * len(songs))
    random_song = songs[random_song_number]
    artist = artists[random_song_number]
    round_no = round_no + 1
    print('Round:',round_no)
    print('Artist:', artist)
    words_of_title = random_song.split()
    for word in words_of_title:
        print(word[0])
    guess = input("Song Name: ")
    if guess == random_song:
        score = score + 3
        print('Correct! Your score is', score)
        print('Next song...')
        print('')
    if guess != random_song:
        loop = 1
        print('Incorrect')
        print('Last Chance')
        print('')
        break

while loop == 1:
    round_no = round_no + 1
    print('Round:',round_no)
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
        loop = 0
    if guess != random_song:
        loop = -1
        print('Incorrect. Score:', score)
        print('Last Chance')
        print('')
        break

while loop == 0:
    random_song_number = int(random() * len(songs))
    random_song = songs[random_song_number]
    artist = artists[random_song_number]
    round_no = round_no + 1
    print('Round:',round_no)
    print('Artist:', artist)
    words_of_title = random_song.split()
    for word in words_of_title:
        print(word[0])
    guess = input("Song Name: ")
    if guess == random_song:
        score = score + 3
        print('Correct! Your score is', score)
        print('Next song...')
        print('')
    if guess != random_song:
        loop = -1
        print('Incorrect')
        print('The song was', random_song)
        print('Total Score:', score)
        break
leaderboard = open("leaderboard.txt", "r+")
leaderboard.write(name + " - " + '{}'.format(score))
leaderboard.close()

print("")
print("Leaderboard:")

leaderboard = open("leaderboard.txt", "r+")
for line in leaderboard:
    print(line, end="")