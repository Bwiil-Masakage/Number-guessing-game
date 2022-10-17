import random
number = random.randint(1, 10)

player_name = input("Hello there, you have a name? ")
number_of_guesses = 0
print('It\'s! a wonderful day to meet you! {} \nLet\'s play a game together, I\'m gonna pick number between 1 and 10 in my mind, then you will guess which number it is, ready? \nDon\'t forget! You only have 3 chances to guess.\n GOODLUCK!:'.format(player_name))

while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your estimate is too low, go up a little!')
    if guess > number:
        print('Your estimate is too high, go down a bit!')
    if guess == number:
        break
if guess == number:
    print( 'Congratulations {}, you guessed the number right in {} tries!'.format(player_name, number_of_guesses))
else:
    print('Oh snap! You couldn\'t guess the number. \nAnyway, the number was {}. Try again!'.format(number))
