import random

#config
low =1
high = 100
limit = 10

#start game
rand = random.randint(low, high)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

guess = -1
tries = 0

#helper functions
def get_guess():
    while True:
        g = input("Take A Guess: ")

        if g.isnumeric():
            g = int(g)
            return g
        else:
            print("YOU MUST ENTER A NUMBER")

#play the game
while guess != rand and tries < limit:
    guess = get_guess()
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

    tries += 1

#tell the player the outcome
if guess == rand:
    print("Good job boi, you got it!")
else:
    print("YEET, the number was " + str(rand))
