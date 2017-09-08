import random

#config
low =1
high = 100
rand = random.randrange(low, high)
print("I'm thinking of a number from " + str(low) + " to " + str(100) + ".");

guess = -1

while guess != rand:
    guess = input("Take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
    else:
        print("You got it!")

print("Game over")
