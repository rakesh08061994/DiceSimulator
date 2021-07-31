from termcolor import colored
import random

def diceSimulator():
    """ Dice Simulator, print dice number randomly"""
    try:
        dice_number = random.randint(1,6)
        if dice_number == 1:
            one = (" \n  o  \n  ")
            print(colored(f'{one}', 'yellow', attrs=['bold']))
        elif dice_number == 2:
            two = (" o  \n\n    o ")
            print(colored(f'{two}', 'yellow', attrs=['bold']))
        elif dice_number == 3:
            three = (" o   \n    o   \n       o ")
            print(colored(f'{three}', 'yellow', attrs=['bold']))
        elif dice_number == 4:
            four = (" o       o \n\n o       o ")
            print(colored(f'{four}', 'yellow', attrs=['bold']))
        elif dice_number == 5:
            five = (" o       o \n     o     \n o       o ")
            print(colored(f'{five}', 'yellow', attrs=['bold']))
        elif dice_number == 6:
            six = (" o   o   o \n o   o   o  \n o   o   o ")
            print(colored(f'{six}', 'yellow', attrs=['bold']))

    except TypeError:
        print("No input needed! Just run function")


if __name__ == "__main__":
    diceSimulator()
    print(diceSimulator.__doc__)
