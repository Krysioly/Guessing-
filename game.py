# greet player
print("Welcome to guessing game. ")
# get player name
name= input("What is your name? ")
print("{} Im thinking of a number between 1 and 100".format(name))
print("Try to guess my number")
import random
# choose random number between 1 and 100
num= random.randint(1, 100)
guess_tally=0
# repeat forever:
while True:
    #     get guess
    guess= int(input("Your guess?"))
#     if guess is incorrect:
    if guess!= num:
#         give hint
        if guess < num:
            print("to low")
        if guess > num:
            print("to high")
#         increase number of guesses
        guess_tally += 1
    else:
#     else:
#         congratulate player
        print("You Win!!")
        print("You guessed {} times".format(guess_tally))
        break
      