import random
print('Hi!')
print('We are going to play a guess the number game.')
print('I am thinking of a number between 1-20, see if you can guess.')

num = random.randint(1,20)

for i in range(6):
    guess = int(input('Pick a number.'))
    if guess > num:
        print('You guessed too high, try again.')
    if guess < num:
        print('You guessed too low, try again.')
    if guess == num:
        print('You guessed correct!')

        break





