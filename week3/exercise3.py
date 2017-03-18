"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    def numberAsker(message, lowerBound=0.5):
        """Asks for a number, ensuring it is.

        message is a string that will be used to ask for the number.

        lowerBound is a number the input must be above. It will always be an
        int except for in the case where it isn't entered.
        """
        answered = False
        while answered is False:
            answered = True
            inputVar = raw_input(message)
            try:
                inputVar = int(inputVar)
            except:
                try:
                    inputVar = float(inputVar)
                except:
                    answered = False
                    print('Please enter a number!')
            if answered and lowerBound != 0.5 and int(inputVar) <= lowerBound:
                answered = False
                print('Please enter a number larger than the lower bound!')
        return inputVar

    print("\nWelcome to the new and revised guessing game!\n")
    print("Time to set the lower and upper bounds. Please enter integers.\n")
    lowerBound = numberAsker("Enter a lower bound: ")
    upperBound = numberAsker("Enter an upper bound: ", int(lowerBound))
    if type(lowerBound) == int and type(upperBound) == int:
        print('Great! two integers - specifically', end=' ')
    else:
        print("Hmmm, looks like you didn't put in two integers.")
        if type(lowerBound) == type(upperBound):
            print("I've changed them to integers, so now it's", end=' ')
        elif type(lowerBound) == 'float':
            print("I've changed your lower bound", end=' ')
            print("to an integer so now it's", end=' ')
        else:
            print("I've changed your upper bound", end=' ')
            print("to an integer so now it's", end=' ')
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)
    print("a number between {} and {}.".format(lowerBound, upperBound))

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = numberAsker("Guess a number:")
        print("You guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("you got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber > upperBound or guessedNumber < lowerBound:
            print('You must have the IQ of a common houseplant. Try ', end='')
            print('something INSIDE the bounds.')
        elif type(guessedNumber) == 'float':
            print("You are more useless than Anne Frank's drum set. ", end='')
            print(" Try an integer next time.")
        elif guessedNumber < actualNumber:
            print("too small, try again ")
        else:
            print("too big, try again   ")
    return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()
