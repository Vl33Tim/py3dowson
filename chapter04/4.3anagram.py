# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
    print (word)

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)
tryi = int(13)
guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")
    tryi -= 1
    if tryi <= 10:
        print("First letter is ", correct[0])
    if tryi <= 5: 
        print("Second letter is ", correct[1])
    if tryi == 0:
        break
if guess == correct:
    print("That's it!  You guessed it!\n")


print("Thanks for playing.")
print("Your score is {} !".format(tryi))
input("\n\nPress the enter key to exit.")
