#Random number guessing game
import random

randomNumber = random.randint(1,100)
userGuessInt = 0
numberOfGuesses = 1

while userGuessInt != randomNumber:
    userGuess = input("Guess what number I'm thinking of: ")
    userGuessInt = int(userGuess)
    if userGuessInt > randomNumber:
        numberOfGuesses = numberOfGuesses + 1
        print('Oh no, too high!')
    elif userGuessInt < randomNumber:
        numberOfGuesses = numberOfGuesses + 1
        print('Oh no, too low!')
    else:
        print('Amazing! How did you guess that?! And it only took ' + str(numberOfGuesses) + ' guesses.')