# General Notes: You can print multiple variables in one print statement through use of comas
# Must specify: "module.function before import becomes valid, in this case we use random.randint()
# New Syntax:     for x in range(6) - creates line of code to be stated more than once
# New Syntax:   input defaults as a string unless otherwise specified - example: int(input())
# New Syntax:   Create a function using the def command followed by the function name
import random
import math
import time

# Cool Title Graphic
print("***************************************************************************************************************")
print("                                         We Finna roll the dice")
print("***************************************************************************************************************")

# Dice rolling function with statistics attached
# NOTE: All statistics functions included are manual, and would be much simpler if imported by statistics module


def roll_the_dice():
    roller_1 = random.randint(1, 6)
    roller_2 = random.randint(1, 6)
    roller_3 = random.randint(1, 6)
    roller_4 = random.randint(1, 6)
    roller_5 = random.randint(1, 6)
    roller_6 = random.randint(1, 6)
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print("                               Dice RoOooOOOOooooOllinG Tiiiiiiiiiimee")
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print("")
    print("Your six values are:")
    print(roller_1, roller_2, roller_3, roller_4, roller_5, roller_6)
    total = (roller_1 + roller_2 + roller_3 + roller_4 + roller_5 + roller_6)
    print("Total:")
    print(total)
    minimum = min(roller_1, roller_2, roller_3, roller_4, roller_5, roller_6)
    print("Minimum:")
    print(minimum)
    maximum = max(roller_1, roller_2, roller_3, roller_4, roller_5, roller_6)
    print("Maximum:")
    print(maximum)
    range = maximum - minimum
    print("Range:")
    print(range)
    print("Mean:")
    mean = (roller_1 + roller_2 + roller_3 + roller_4 + roller_5 + roller_6)/6
    print(round(mean, 4))
    std = math.sqrt(((roller_1 - mean)**2 + (roller_2 - mean)**2 + (roller_3 - mean)**2 + (roller_4 - mean)**2 + \
                    (roller_5 - mean)**2 + (roller_6 - mean)**2)/5)
    print("Standard Deviation:")
    print(round(std, 4))


# Ask user if they want to roll the dice


print("Roll The Dice? (0=No, 1=Yes)")
roll = int(input(": "))
if roll == 1:
    time.sleep(1)
    roll_the_dice()
else:
    print("lmao too bad, we're rolling the dice anyway")
    time.sleep(1)
    roll_the_dice()

# Pause the program so it doesn't shutdown immediately

time.sleep(15)