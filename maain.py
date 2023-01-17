import random
#importing random and writting a while loop
number=random.randint(1,10)
print(number)
isGuessRight = False
# while isGuessRight != True:
#     guess = input("Guess a number between 1 and 10: ")
#     if int(guess) == number:
#         print("You guessed {}. That is correct! You win!".format(guess))
#         isGuessRight = True
#     else:
#         print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("you guessed {}. That is correct! you win!".format(guess))
        isGuessRight = True
    else:
        print("you guessed {}. That is not it. Try again.".format(guess))
print("Count to 10!")
for x in range(0,11):
    print(x)