# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""
from __future__ import division
from __future__ import print_function
import math
# import time


def binary_search(low, high, actual_number, counter=0):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    Each guess, print what the guess is Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    This will be quite hard, especially hard if you don't have a good diagram!

    Debugging helpers:
      * GUARD is there to make it only run a few times so that you can see
        what's happening.
      * time.sleep(0.5) makes it pause for half a second.
      You don't need to use both together, and should remove them both before
      you submit. The tests will be checking that they aren't in there.
      (You should remove them from the file, not comment them out, the
      tests aren't that smart yet.)
    """
    if int((low + high)/2) == actual_number:
        return {"guess": actual_number, "tries": counter}
    elif int((low + high)/2) > actual_number:
        return binary_search(low, (low+high)/2, actual_number, counter+1)
    else:
        return binary_search((low+high)/2, high, actual_number, counter+1)

    # midpoint = (low + high) / 2
    # if actual_number == midpoint:
    #     return {"guess": actual_number, "tries": tries}
    # elif midpoint


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
