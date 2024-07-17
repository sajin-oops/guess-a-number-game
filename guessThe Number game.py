import random
num = random.randint(1,20)
print(num)
guess = int(input("Guess a number between 1 and 20: "))
while guess != num:
    if guess > num:
        print("Your guess is too high")
        guess = int(input("Guess again: "))
    else:
        print("Your guess is too low")
        guess = int(input("Guess again: "))
print("Good Job, You won the game")
# output
'''
17
Guess a number between 1 and 20: 17
Good Job, You won the game
'''