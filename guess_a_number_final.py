import random
import math

# config
low = 1
high = 10
limit = int(round(math.log(high, 2)))

# helper functions
def show_start_screen():
    print("       ___           ___           ___           ___           ___                    ___                    ___           ___           ___           ___           ___           ___     ")
    print("      /\  \         /\__\         /\  \         /\  \         /\  \                  /\  \                  /\__\         /\__\         /\__\         /\  \         /\  \         /\  \    ")
    print("     /::\  \       /:/  /        /::\  \       /::\  \       /::\  \                /::\  \                /::|  |       /:/  /        /::|  |       /::\  \       /::\  \       /::\  \   ")
    print("    /:/\:\  \     /:/  /        /:/\:\  \     /:/\ \  \     /:/\ \  \              /:/\:\  \              /:|:|  |      /:/  /        /:|:|  |      /:/\:\  \     /:/\:\  \     /:/\:\  \  ")
    print("   /:/  \:\  \   /:/  /  ___   /::\~\:\  \   _\:\~\ \  \   _\:\~\ \  \            /::\~\:\  \            /:/|:|  |__   /:/  /  ___   /:/|:|__|__   /::\~\:\__\   /::\~\:\  \   /::\~\:\  \ ")
    print("  /:/__/_\:\__\ /:/__/  /\__\ /:/\:\ \:\__\ /\ \:\ \ \__\ /\ \:\ \ \__\          /:/\:\ \:\__\          /:/ |:| /\__\ /:/__/  /\__\ /:/ |::::\__\ /:/\:\ \:|__| /:/\:\ \:\__\ /:/\:\ \:\__\ ")
    print("  \:\  /\ \/__/ \:\  \ /:/  / \:\~\:\ \/__/ \:\ \:\ \/__/ \:\ \:\ \/__/          \/__\:\/:/  /          \/__|:|/:/  / \:\  \ /:/  / \/__/~~/:/  / \:\~\:\/:/  / \:\~\:\ \/__/ \/_|::\/:/  /")
    print("   \:\ \:\__\    \:\  /:/  /   \:\ \:\__\    \:\ \:\__\    \:\ \:\__\                 \::/  /               |:/:/  /   \:\  /:/  /        /:/  /   \:\ \::/  /   \:\ \:\__\      |:|::/  / ")
    print("    \:\/:/  /     \:\/:/  /     \:\ \/__/     \:\/:/  /     \:\/:/  /                 /:/  /                |::/  /     \:\/:/  /        /:/  /     \:\/:/  /     \:\ \/__/      |:|\/__/  ")
    print("     \::/  /       \::/  /       \:\__\        \::/  /       \::/  /                 /:/  /                 /:/  /       \::/  /        /:/  /       \::/__/       \:\__\        |:|  |    ")
    print("      \/__/         \/__/         \/__/         \/__/         \/__/                  \/__/                  \/__/         \/__/         \/__/         ~~            \/__/         \|__|    ")
def show_credits():
    print()
    print("      ___           ___           ___           ___                    ___           ___          _____          ___          _____    ")
    print("     /  /\         /  /\         /__/\         /  /\                  /  /\         /__/\        /  /::\        /  /\        /  /::\   ")
    print("    /  /:/_       /  /::\       |  |::\       /  /:/_                /  /:/_        \  \:\      /  /:/\:\      /  /:/_      /  /:/\:\  ")
    print("   /  /:/ /\     /  /:/\:\      |  |:|:\     /  /:/ /\              /  /:/ /\        \  \:\    /  /:/  \:\    /  /:/ /\    /  /:/  \:\ ")
    print("  /  /:/_/::\   /  /:/~/::\   __|__|:|\:\   /  /:/ /:/_            /  /:/ /:/_   _____\__\:\  /__/:/ \__\:|  /  /:/ /:/_  /__/:/ \__\:| ")
    print(" /__/:/__\/\:\ /__/:/ /:/\:\ /__/::::| \:\ /__/:/ /:/ /\          /__/:/ /:/ /\ /__/::::::::\ \  \:\ /  /:/ /__/:/ /:/ /\ \  \:\ /  /:/ ")
    print(" \  \:\ /~~/:/ \  \:\/:/__\/ \  \:\~~\__\/ \  \:\/:/ /:/          \  \:\/:/ /:/ \  \:\~~\~~\/  \  \:\  /:/  \  \:\/:/ /:/  \  \:\  /:/  ")
    print("  \  \:\  /:/   \  \::/       \  \:\        \  \::/ /:/            \  \::/ /:/   \  \:\  ~~~    \  \:\/:/    \  \::/ /:/    \  \:\/:/  ")
    print("   \  \:\/:/     \  \:\        \  \:\        \  \:\/:/              \  \:\/:/     \  \:\         \  \::/      \  \:\/:/      \  \::/   ")
    print("    \  \::/       \  \:\        \  \:\        \  \::/                \  \::/       \  \:\         \__\/        \  \::/        \__\/    ")
    print("     \__\/         \__\/         \__\/         \__\/                  \__\/         \__\/                       \__\/                  ")
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print()
            print("You must enter a number.")

def pick_number():
    print()
    print("I'm thinking of a number from " + str(low) + " to " + str(high) + ". You have " + str(limit) + " tries.")

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print()
        print("You guessed too low.")
    elif guess > rand:
        print()
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print()
        print("You win!")
    else:
        print()
        print("You are such a loser! The number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print()
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
