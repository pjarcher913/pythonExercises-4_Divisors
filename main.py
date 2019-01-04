# Created by:   Patrick Archer
# Date:         20 December 2018
# Copyright to the above author. All rights reserved.

"""
Directions - COMPLETE:
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a
divisor of 26 because 26 / 13 has no remainder.)

"""

# ################################################# start_funcs

def calcDivisors(userDivisor, maxRangeValue):
    divRange = range(1, maxRangeValue + 1)
    divResults = []

    for n in range(len(divRange)):
        if (divRange[n] % userDivisor == 0):
            divResults.append(divRange[n])

    return divResults

# ################################################# end_funcs/start_main

userNum = input("\nPlease enter the number you wish to show all divisors for.\n")
userMaxRange = input("Please enter the max number you want your divisor modded against\n"
                     "(i.e., the max value for the integer range your requested divisor will be compared against).\n")

# try to convert userNum from str to int; catch errors
try:
    userNum = int(userNum)
    userMaxRange = int(userMaxRange)
except (ValueError):
    print("\n<ERROR>: Invalid value entered. Ending program to prevent catastrophe. Please try again.\n")

print("\n<CONSOLE>: Now executing calculations. Results are below.\n")

results = calcDivisors(userNum, userMaxRange)

print("Resulting whole divisors: \n" + str(results))

# ################################################# end_main







