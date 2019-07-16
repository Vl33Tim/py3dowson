# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = -1
tries = 1
top = 100
bot = 1

def ask_number(question = "Take a guess beetween (1 - 100):",low = 1, high = 100,step = 1):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high,step):
        response = int(input(question))
    return response

# guessing loop
while guess != the_number:
    #guess = ask_number()
    if guess > the_number:
        top = guess
        guess = ask_number(low = bot, high = top)
        print("Lower...")
        print("Between {} and {}".format(bot,top))
    else:
        bot = guess
        guess = ask_number(low = bot, high = top)
        print("Higher...")
        print("Between {} and {}".format(bot,top))
            
    #guess = int(input("Take a guess: "))
    tries += 1

print("You guessed it!  The number was", the_number)
print("And it only took you", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
