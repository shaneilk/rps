import random
import string

#gets a random number and mods it by three
def getName():
    truth = False
    while(truth == False):
        name = input("Please enter your name: ")
        tmp = input(name + " what a fine name, is that the name you would like to choose? (T or F): ")
        if(tmp == "T"):
            truth = True
        else:
            truth = False
    return name

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
        choice = input("Enter a valid Choice (Rock, Paper or Scissors): ")
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
        print("Elon wins! as " + elonObj + " beats " + playerObj)
    else:
        print(str(name) + " wins! as " + str(playerObj) + " beats " + str(elonObj))
    
# essentially the main program
def playingGame():
    name = getName()
    truth = True
    while(truth):
        playerObj = playerChoice()
        elonObj = elonChoice()
        battle(name, playerObj, elonObj)
        tmp = input("would you like to keep playing? (Y/N)")
        if(tmp == "Y"):
            truth = True
        else:
            truth = False
    print("Thank you for playing, I hope to play with you again")

playingGame()
