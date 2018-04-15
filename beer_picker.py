import random
import os

"""
Created on Sunday the 15'th of April 2018 at 04:01 AM

Takes raw input specifying how many beers a person has to choose from and what their names are and selects a beer, that
the person has to drink.

@author Rune "Ion" N. T. Thorsen
"""


def pick_a_random_beer():
    """
    This method takes raw input as the number of beers to choose from and their name and prints the name of a beer a user should drink
    """
    os.system("clear")

    n = int(raw_input("Type the number of beers you have to choose from: "))

    os.system("clear")

    beers = []

    for i in range(n - 1):
        beers.append(raw_input("Give a name for one of the beers you have to choose from: "))

    os.system("clear")
    print("You should drink a %s" % (beers[random.randint(0, n-1)]))


def main():
    pick_a_random_beer()


if __name__ == '__main__':
    main()
