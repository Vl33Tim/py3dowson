# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in a five attempts.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number and tries != 5:
    if guess > the_number:
        print("Lower, {} tries have left".format(tries))
    else:
        print("Higher, {} tries have left".format(tries))
    guess = int(input("Take a guess: "))
    tries += 1
if tries == 5:
    print("Game over, the number was ", the_number)
else:
    print("You guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
