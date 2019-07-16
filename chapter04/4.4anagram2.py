#anagram version 2.0
import random

WORDS = ("python","programming","linux","computer","django")

word = random.choice(WORDS)
CORRECT = word

jumble=""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position +1):]
lenght = len(jumble)
print("Welcome to game jumble,\n word has {} letters".format(lenght))

for i in range(5,0,-1):
    print("You have {} tries".format(i))
    guess = input("Take your guess\n")
    for i in guess.lower():
        if i in CORRECT:    
            print("\nThere are letter match have founded")
            break
        
    if i not in CORRECT:
        print("\nNo matches founded")

print("\nTo exit press enter")

while guess != CORRECT:
    guess = input("Make your guess.\n")
    if guess == "":
        break
if guess == CORRECT:
    input("You win, the name was {}, press ENTER to exit".format(CORRECT))
else:
    input("Thank you for playing")




