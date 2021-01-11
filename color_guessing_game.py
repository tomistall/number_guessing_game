import random

#print(secret_color)

color = ["red", "yellow", "blue"]
secret_color = random.choice(color)
userGuess = ""
numberOfGuesses = 1

while userGuess != secret_color:
    userGuess = raw_input("Guess a primary color: ")
    if userGuess.lower() != secret_color:
        print("Hmmm... that's not right.")
        numberOfGuesses = numberOfGuesses + 1
    else:
        if numberOfGuesses == 1:
            print("Wooo! You're right. It only took you " + str(numberOfGuesses) + ' guess.')
            numberOfGuesses = numberOfGuesses + 1
            break
        else:
            print("Wooo! You're right. It only took you " + str(numberOfGuesses) + ' guesses.')
            numberOfGuesses = numberOfGuesses + 1
            break