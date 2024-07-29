# -------------------------------------------------------------------
# Libraries
# -------------------------------------------------------------------
import random

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# Variables
user = ""
points = 0
play = True
win = False
new = True
auth = False

# Lists
used = []
ranking = [["", 0], ["", 0], ["", 0], ["", 0], ["", 0]]

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# Function to get the first letter of each word in the song name
def first_letters(words):
    hold = ""
    for i in range(len(words)):
        hold = hold + (words[i][0]+"- ")
    return hold

# Function to get the number of lines in the songs.txt file
def len_songs():
    song = open("songs.txt", "r")
    length = len(song.readlines())
    song.close()
    return length

# Function to get the number of lines in the scores.txt file
def len_scores():
    score = open("scores.txt", "r")
    length = int(len(score.readlines()))
    score.close()
    return length

# Function to read every line of scores.txt and determining the top 5 scores for displaying
def ranks():
    score = open("scores.txt", "r")

    for i in range(len_scores()):
        line = score.readline()
        new = line.split(", ")
        num = int(new[1])

        # The list of rankings are ordered in descending order using the bubble sort method
        if num >= int(ranking[0][1]):
            ranking[4] = ranking[3]
            ranking[3] = ranking[2]
            ranking[2] = ranking[1]
            ranking[1] = ranking[0]
            ranking[0] = new

        elif num >= int(ranking[1][1]):
            ranking[4] = ranking[3]
            ranking[3] = ranking[2]
            ranking[2] = ranking[1]
            ranking[1] = new

        elif num >= int(ranking[2][1]):
            ranking[4] = ranking[3]
            ranking[3] = ranking[2]
            ranking[2] = new

        elif num >= int(ranking[3][1]):
            ranking[4] = ranking[3]
            ranking[3] = new

        elif num >= int(ranking[4][1]):
            ranking[4] = new

    score.close()

    # The rankings are displayed
    # If the rank slot isn't filled it will not be displayed
    if ranking[0][0] != "":
        print("\nFirst: {}, {}".format(ranking[0][0], ranking[0][1].strip()))

    if ranking[1][0] != "":
        print("\nSecond: {}, {}".format(ranking[1][0], ranking[1][1].strip()))

    if ranking[2][0] != "":
        print("\nThird: {}, {}".format(ranking[2][0], ranking[2][1].strip()))

    if ranking[3][0] != "":
        print("\nFourth: {}, {}".format(ranking[3][0], ranking[3][1].strip()))

    if ranking[4][0] != "":
        print("\nFifth: {}, {}".format(ranking[4][0], ranking[4][1].strip()))

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# Authorising the user
while not auth:
    user = input("What is your name? ")

    if user != "":
        auth = True

# Parameters which need to be met for the game to continue
while play and not win:

    new = True
    while new:  # checks whether the random number has been used before
        rand = random.randint(1, len_songs())
        if rand not in used:
            new = False

        # if all the songs have been asked the user has beat the game
        elif len(used) == len_songs()-1:
            win = True

    # adding the newest random number to the 'used' list
    used.append(rand)

    # The song file in opened and randomly picked line is read
    song = open("songs.txt", "r")
    for x in range(rand):
        line = song.readline()
    song.close()
    # The name and artist of the song are separated and stored as a list
    answer = line.split(", ")
    # The '\n' is removed from the end of the artist's name
    answer[1] = answer[1].strip()
    artist = answer[1]
    # Every word of the name is separated into items of a list
    name = answer[0]
    name_words = name.split(" ")

    # The question is asked and an answer is received
    print("{} by {} ".format(first_letters(name_words), artist))
    guess = input("What is the name of the song? ")

    # If the guess is correct the first time
    if guess == name:
        print("WELL DONE! You got 3 points\n")
        points = points + 3

    # If the guess is incorrect the first time trigger the question again
    elif guess != name:
        print("INCORRECT! You get one more guess")
        guess = input("What is the name of the song? ")

        # If the guess is correct
        if guess == name:
            print("WELL DONE! You got 1 point\n")
            points = points + 1

        # If the guess is incorrect
        else:
            print("GAME OVER!")
            play = False  # If the guess is incorrect twice the game ends

# If the user has won the game display a congratulations message
if win:
    print("You got everything right!")

# The user is told how many points they got
print("You got", points, "points!")

# If the user doesn't get any points their score isn't added to the scores file
if points > 0:
    score = open("scores.txt", "a")
    score.write("{}, {}\n".format(user, points))
    score.close()

ranks()