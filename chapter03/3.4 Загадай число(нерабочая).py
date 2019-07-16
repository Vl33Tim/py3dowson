import random  

print("\tWelcome to 'Think of a number!'")
print("\nPlease think of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = int(input("Enter the number "))
bot_border = 1 #нижняя граница диапазона возможных чисел
top_border = 100 #верхняя граница диапазона чисел
tries = 1
guess = 0

guess = random.randint(bot_border, top_border)


# guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower than", top_border)
        top_border = guess#(guess - 1)
    elif guess < the_number:
        print("Higher than", bot_border)
        bot_border = guess#(guess  + 1)

    guess = random.randint(bot_border, top_border)
    tries += 1

print("Programm guessed it!  The number was ", the_number)
print("And it only took it ", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
