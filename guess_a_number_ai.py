#
#Guess a Number AI
#Ryan Woods
#9/29/17

import random
import math

# config

def get_range():
    print()
    low = input("Create a low value: ")
    print()
    high = input("Create a High Value: ")
    
    return int(low), int(high)

#limit = int(round(math.log(high, 2)))

# helper functions
def show_start_screen():
    print("   _______  __    __   _______     _______.     _______.        ___         .__   __.  __    __  .___  ___. .______    _______ .______                       ___       __   __  ")
    print("  /  _____||  |  |  | |   ____|   /       |    /       |       /   \        |  \ |  | |  |  |  | |   \/   | |   _  \  |   ____||   _  \                     /   \     |  | |  | ")
    print(" |  |  __  |  |  |  | |  |__     |   (----`   |   (----`      /  ^  \       |   \|  | |  |  |  | |  \  /  | |  |_)  | |  |__   |  |_)  |                   /  ^  \    |  | |  | ")
    print(" |  | |_ | |  |  |  | |   __|     \   \        \   \         /  /_\  \      |  . `  | |  |  |  | |  |\/|  | |   _  <  |   __|  |      /                   /  /_\  \   |  | |  | ")
    print(" |  |__| | |  `--'  | |  |____.----)   |   .----)   |       /  _____  \     |  |\   | |  `--'  | |  |  |  | |  |_)  | |  |____ |  |\  \____.__ __ __     /  _____  \  |  | |__| ")
    print("  \______|  \______/  |_______|_______/    |_______/       /__/     \__\    |__| \__|  \______/  |__|  |__| |______/  |_______|| _| `._____(__|__|__)   /__/     \__\ |__| (__) ")
    print()
def show_credits():
    print()
    print("this awesome game was coded by Ryan on 9/29/17")
    
def get_guess(current_low, current_high):
    guess = (current_low + current_high) // 2
    return guess

def pick_number(low,high,name):
    print()
    input("OK, " + str(name) + ", Think of a number in between " + str(low) + " and " + str(high) + ", then press enter...")
    

def check_guess(guess, tries):
    print()
    print("For attempt # " + str(tries + 1) + " is your number " + str(guess) + "?")
    print()
    playerinput = input("Was I too high/too low/ or correct  ")
    playerinput = playerinput.lower()
    if playerinput == "too low" or playerinput == "l" or playerinput == "low":
        return -1
    elif playerinput == "too high" or playerinput == "h" or playerinput == "high":
        return 1
    elif playerinput == "correct" or playerinput == "c":
        return 0
    else:
        print ("please type either too high, too low, or correct")

def show_result(guess,tries,name):
    print()
    print(" ____    ____  _______  _______ .___________. ")
    print(" \   \  /   / |   ____||   ____||           | ")
    print("  \   \/   /  |  |__   |  |__   `---|  |----` ")
    print("   \_    _/   |   __|  |   __|      |  |     ")
    print("     |  |     |  |____ |  |____     |  |     ")
    print("     |__|     |_______||_______|    |__|     ")
    print()
    print("lol @" + str(name) + ", i is so smert, i got it in " + str(tries) + " attempts.")
    print()
    
def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    tries = 0
    current_low,current_high = get_range()
    check = -1
    limit = int(round(math.log(current_high - current_low + 1, 2)))
    
    pick_number(current_low,current_high,name)
    
    while check != 0 and check < limit:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess, tries)

        if check == -1:
            current_low = int(guess)
        
            
        elif check == 1:
            current_high = int(guess)

        tries += 1
            

    show_result(guess,tries,name)


# Game starts running here
show_start_screen()

playing = True

name = input("WHAT BE THOUST NAME? ")

while playing:
    play()
    playing = play_again()

show_credits()



