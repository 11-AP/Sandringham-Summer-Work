# -------------------------------------------------------------------
# Libraries
# -------------------------------------------------------------------
import random

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# Variables
player1 = ""
player2 = ""
p1_score = 0
p2_score = 0
die1 = 0
die2 = 0
die3 = 0
total = 0
auth1 = False
auth2 = False
winner = False

# Lists
ranking = [["", 0], ["", 0], ["", 0], ["", 0], ["", 0]]
# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# Function to generate a random number between 1 and 6
def roll():
    rand = random.randint(1,6)
    return rand

# Function to represent one round for one player
def round(name):
    # Dice values are set and total is calculated
    die1 = roll()
    die2 = roll()
    total = die1 + die2
    print("\n{} ROLLS {} AND {}".format(name, die1, die2))

    # Checking if the total is even
    if total % 2 == 0:
        print("\nThat's EVEN +10 points")
        total = total + 10

    # Checking if the total is odd
    elif total % 2 != 0:
        print("\nThat's ODD -5 points")
        total = total - 5

    # Checking if a double was rolled
    if die1 == die2:
        die3 = roll()
        print("\nYOU ROLLED A DOUBLE")
        print("+{} points".format(die3))
        total = total + die3

    return total

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
# Checking that the usernames inputted are valid
while not auth1:
    player1 = input("Player 1 what is your name? ")

    if player1 != "":
        auth1 = True

while not auth2:
    player2 = input("Player 2 what is your name? ")

    if player2 != "":
        auth2 = True

# A for loop to repeat the round function for each player 5 times
for i in range(5):
    p1_score = p1_score + round(player1)

    # Checking if the player score dropped below 0
    if p1_score < 0:
        p1_score = 0

    p2_score = p2_score + round(player2)

    # Checking if the player score dropped below 0
    if p2_score < 0:
        p2_score = 0

# Player results revealed
print("\n{} got {}".format(player1, p1_score))
print("\n{} got {}".format(player2, p2_score))

# Making sure there is a winner
while not winner:
    if p1_score > p2_score:
        print("{} WINS with {} points!".format(player1, p1_score))
        score = open("scores.txt", "a")
        score.write("{}, {}\n".format(player1, p1_score))
        score.close()
        winner = True

    elif p1_score < p2_score:
        print("{} WINS with {} points!!".format(player2, p2_score))
        score = open("scores.txt", "a")
        score.write("{}, {}\n".format(player2, p2_score))
        score.close()
        winner = True

    # If there is a draw giving each player one more roll
    else:
        print("It's a DRAW! ")
        p1_score = p1_score + roll()
        p2_score = p2_score + roll()

# Getting and displaying the ranks from scores.txt
ranks()