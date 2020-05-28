# import random num package
import random

# Variable keeping track if app is running
isRunning = True


# Dice roll function
def role_dice(dice_type, times):

    for x in range(times):
        rolled_num = random.randint(1, dice_type)
        print("roll " + str(x+1) + ": " + str(rolled_num))
        print


# Main program thread
print
print("Welcome to Daniel's Dice Roller")
print("-------------------------------")

# while isRunning = true
while isRunning:

    dice_choice = input("What kind of dice would you like to roll?  ")

    # Check if the user wants to exit the program
    if dice_choice == "exit" or dice_choice == 0:
        print("-----------")
        print("| goodbye |")
        print("-----------")
        break

    times = input("How may times would you like to roll this dice?  ")
    print

    role_dice(dice_choice, times)
