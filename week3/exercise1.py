# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""
from __future__ import division
from __future__ import print_function


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    new_list = []
    while start < stop:
        new_list.append(start)
        start += step
    return new_list


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    return range(start, stop, step)


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    return range(start, stop, 2)


def gene_krupa_range(start, stop, even_step, odd_step):
    """Make a range that has two step sizes.

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """
    range_list = []
    counter = 1
    while start <= stop:
        range_list.append(start)
        if counter % 2 == 1:
            start += even_step
        else:
            start += odd_step
        counter += 1
    return range_list

    # gene_list = []
    # latest = start
    # count = 0
    # while latest < stop:
    #     gene_list.append(latest)
    #     if beat % 2 == 0:
    #         latest += even_step
    #     else:
    #         latest = odd_step
    #     beat = beat + 1
    # return gene_list

    """Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    message = "number between {low} and {high}:".format(low=low, high=high)

    while True:
        input_number = int(raw_input(message))
        if low < input_number < high:
            print("good {} looks good!".format(input_number))
            return input_number
        else:
            print("{input} isn't between {low}, and {high}".format(
                                    input=input_number, low=low, high=high))
        print(low < input_number, input_number < high)

        input_number = int(raw_input(message))
        print(low < input_number < high)


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    message = "Give me  number"

    while True:
        try:
            input_number = int(raw_input(message))
            print("thanks! {} looks good".format(input_number))
            return input_number
        except Exception as e:
            print("try agian ({})".format(e))


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    message = ("Type a number between {} and {}:".format(low, high))
    while True:
            while True:
                try:
                    input_number = int(raw_input(message))
                    print("{}is a number".format(input_number))
                    if low < input_number < high:
                        print("{} is vaild".format(input_number))
                        return(input_number)
                    else:
                        print("{} is not vaild".format(input_number))
                except Exception as e:
                    print("Try again ({})".format(e))

    return(input_number)
    # message = "give me a number between {} and {}:".format(low, high)
    #
    # answered = False
    # while answered is False:
    #     answered = True
    #     num = raw_input("type number between {} and {}".format(low, high))
    #
    # while True:
    #         try:
    #             i_no = int(raw_input(message))
    #             if low < i_no < high:
    #                 print("correct {}").format(i_no)
    #                 return i_no
    #             else:
    #                 print("{}incorrect, not between {} and {}")


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    # inside Atom, you need to run them from the terminal. E.g.:
    # ben@um:~/projects/git/code1161base$ python week3/exercise1.py

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Give me a number")
    print("\nsuper_asker")
    super_asker(33, 42)
