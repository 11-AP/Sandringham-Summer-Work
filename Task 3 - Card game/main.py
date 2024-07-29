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
auth1 = False
auth2 = False
play = True
new = False

# Lists
cards = [["red", 1], ["red", 2], ["red", 3], ["red", 4], ["red", 5], ["red", 6], ["red", 7], ["red", 8], ["red", 9],
          ["red", 10], ["yellow", 1], ["yellow", 2], ["yellow", 3], ["yellow", 4], ["yellow", 5], ["yellow", 6],
          ["yellow", 7], ["yellow", 8], ["yellow", 9], ["yellow", 10], ["black", 1], ["black", 2], ["black", 3],
          ["black", 4], ["black", 5], ["black", 6], ["black", 7], ["black", 8], ["black", 9], ["black", 10]]
deck =[]
used = []
p1 = []
p2 = []
picks1 = []
picks2 = []
ranking = [["", 0], ["", 0], ["", 0], ["", 0], ["", 0]]

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# Function to get the number of lines in the winners.txt file
def len_winners():
    winner = open("winners.txt", "r")
    length = int(len(winner.readlines()))
    winner.close()
    return length

# Function to read every line of winners.txt and determining the top 5 winners for displaying
def ranks():
    winner = open("winners.txt", "r")

    for i in range(len_winners()):
        line = winner.readline()
        hold = line.split(", ")
        num = int(hold[1])

        # The list of rankings are ordered in descending order using the bubble sort method
        if num >= int(ranking[0][1]):
            ranking[4] = ranking[3]
            ranking[3] = ranking[2]
            ranking[2] = ranking[1]
            ranking[1] = ranking[0]
            ranking[0] = hold

        elif num >= int(ranking[1][1]):
            ranking[4] = ranking[3]
            ranking[3] = ranking[2]
            ranking[2] = ranking[1]
            ranking[1] = hold

        elif num >= int(ranking[2][1]):
            ranking[4] = ranking[3]
            ranking[3] = ranking[2]
            ranking[2] = hold

        elif num >= int(ranking[3][1]):
            ranking[4] = ranking[3]
            ranking[3] = hold

        elif num >= int(ranking[4][1]):
            ranking[4] = hold

    winner.close()

    # The rankings are displayed
    # If the rank slot isn"t filled it will not be displayed
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

# Adding all the items in the 'cards' list into 'deck' list in a random order to represent shuffling cards
for i in range(30):
    new = False
    while not new:
        rand = random.randint(0, 29)

        if rand not in used:
            new = True
            used.append(rand)
            deck.append(cards[rand])

# Distributing the cards between the 2 players
for x in range(30):
    if x % 2 == 0:  # All items with an even index go to player 1
        picks1.append(deck[x])
    elif x % 2 != 0:  # All items with an odd index go to player 2
        picks2.append(deck[x])

# A loop to so all 15 rounds of the game are played
for i in range(15):
    # Displaying to the players what cards the pulled
    print("\n{} pulled a {} {}".format(player1, picks1[i][0], picks1[i][1]))
    print("{} pulled a {} {}".format(player2, picks2[i][0], picks2[i][1]))

    if picks1[i][0] == picks2[i][0]:  # Check if the colours of the cards are the same
        if picks1[i][1] > picks2[i][1]:  # Comparing the number on the cards
            print("\n" + player1 + " TAKES!")
            p1.append(picks1[i])
            p1.append(picks2[i])

        else:
            print("\n" + player2 + " TAKES!")
            p2.append(picks1[i])
            p2.append(picks2[i])

    else:
        if picks1[i][0] == "red" and picks2[i][0] == "black":  # P1 TAKES
            print("\n" + player1 + " TAKES!")
            p1.append(picks1[i])
            p1.append(picks2[i])

        elif picks1[i][0] == "black" and picks2[i][0] == "red":  # P2 TAKES
            print("\n" + player2 + " TAKES!")
            p2.append(picks1[i])
            p2.append(picks2[i])

        elif picks1[i][0] == "red" and picks2[i][0] == "yellow":  # P2 TAKES
            print("\n" + player2 + " TAKES!")
            p2.append(picks1[i])
            p2.append(picks2[i])

        elif picks1[i][0] == "yellow" and picks2[i][0] == "red":  # P1 TAKES
            print("\n" + player1 + " TAKES!")
            p1.append(picks1[i])
            p1.append(picks2[i])

        elif picks1[i][0] == "yellow" and picks2[i][0] == "black":  # P2 TAKES
            print("\n" + player2 + " TAKES!")
            p2.append(picks1[i])
            p2.append(picks2[i])

        elif picks1[i][0] == "black" and picks2[i][0] == "yellow":  # P1 TAKES
            print("\n" + player1 + " TAKES!")
            p1.append(picks1[i])
            p1.append(picks2[i])

# Displaying the number of cards each player has by the end fo the game.
print("\n{} has {} cards".format(player1, len(p1)))
print("{} has {} cards".format(player2, len(p2)))

# Comparing which player has the most cards
if len(p1) > len(p2):
    score = open("winners.txt", "a")
    score.write("{}, {}\n".format(player1, len(p1)))
    score.close()
    print("\n{} WINS with {} cards!!".format(player1, len(p1)))

elif len(p1) < len(p2):
    score = open("winners.txt", "a")
    score.write("{}, {}\n".format(player2, len(p2)))
    score.close()
    print("\n{} WINS with {} cards!!".format(player2, len(p2)))

else:
    print("\nIt's a DRAW! ")

# Display the top 5 winners
ranks()
