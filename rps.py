import random
import string

#gets a random number and mods it by three
def getName():
    truth = False
    while(truth == False):
        name = input("What is your name?: ")
        tmp = input(name + " what a fine name, is that the name you would like to choose? (Yes or No): ")
        tmp = tmp.lower()
        if(tmp == "yes"):
            truth = True
        elif(tmp == "no"):
            truth = False
    return name

def greeting():
    print("\nHello There! and welcome to our game of Rock, Paper, Scissors.") 
    print("My name is Elon Nye, C.E.O. of Nye Motors and your opponent for this game.")

#using a rng gets a random number and mods it by 3 to pick between rock paper and scissors
def randomChoice():
    choice = random.randint(0,81240806)
    choice = choice % 3
    ls = ["rock", "paper", "scissors"]
    return ls[choice]

#checks if the parameter string is a valid input
def validChoice(choice):
    choice = choice.lower()
    ls = ["rock", "paper", "scissors"]
    for i in range(3):
        if(choice == ls[i]):
            return True
    return False

#generates a rock paper or scissors choice for Elon (CPU)
def elonChoice():
    choice = randomChoice()
    ls = ["rock", "paper", "scissors"]
    for i in range(3):
        if(choice == ls[i]):
            return choice

#asks player for a valid input 
def playerChoice():
    valid = False
    while(valid == False):
        choice = input("Choose your object! (Rock, Paper or Scissors): ")
        valid = validChoice(choice)
    return choice.lower()

#compares two choices (rock paper or scissors) and based on object chosen it decides whether elon or the player wins, if a tie 
#keep asking for player to choose an object
def battle(name,  playerObj, elonObj):
    while(playerObj == elonObj):
        print("WE HAVE A TIE! as " + name + " and Elon both chose " + playerObj + "\n")
        print("Pick another Object!\n")
        playerObj = playerChoice()
        elonObj = elonChoice()

    ls = []
    if(playerObj == "rock"):
        ls = ["paper", "scissors"]
    elif(playerObj == "paper"):
        ls = ["scissors", "rock"]
    elif(playerObj == "scissors"):
        ls = ["rock", "paper"]
    if(elonObj == ls[0]):
        print("Elon wins! as " + elonObj + " beats " + name + "'s " + playerObj + "\n")
    else:
        print(str(name) + " wins! as " + str(playerObj) + " beats Elon's " + str(elonObj) + "\n")
    
# essentially the main program
def playingGame():
    greeting()
    name = getName()
    truth = True
    while(truth):
        tmp = ("string")
        playerObj = playerChoice()
        elonObj = elonChoice()
        battle(name, playerObj, elonObj)
        while(not(tmp == "yes") and not(tmp == "no")):
            tmp = input("would you like to keep playing? (Yes or No): ")
            tmp = tmp.lower()
            if(tmp == "yes"):
                truth = True
            elif(tmp == "no"):
                truth = False
    print("Thank you for playing, I hope to play with you again!\n")

playingGame()
