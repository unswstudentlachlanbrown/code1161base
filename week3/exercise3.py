"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
from exercise1 import not_number_rejector
from exercise1 import super_asker
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
    print("\nwelcome to the guessing game!")

    lowerbound = not_number_rejector("Enter a lower bound: ")
    while True:
        upperbound = not_number_rejector("Enter a upper bound: ")
        if upperbound <= lowerbound:
            print ("Type in a number over {}".format(upperbound))
        elif upperbound == lowerbound + 1:
            print ("Type in a number over {}".format(upperbound))
        elif lowerbound >= upperbound:
            print("{} is incorrect, please do one bellow upperbound"
                  .format(lowerbound))
        else:
            print("go ahead")
            break

    actual_number = random.randint(lowerbound, upperbound)

    guessed = False
    while not guessed:
        guess_number = super_asker(lowerbound, upperbound)
        print("You guessed {}".format(guess_number),)
        if guess_number == actual_number:
            print("{}, You guessed correctly".format(actual_number))
            guessed = True
        elif guess_number < actual_number:
            print("incorrect, try larger number")
        else:
            print("incorrect, try smaller number")
    return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()
