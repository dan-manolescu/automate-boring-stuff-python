#! python3
# debugTest.py - Just a test for debugging.

import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()
toss = 'tails' if random.randint(0, 1) == 0 else 'heads'  # 0 is tails, 1 is heads
logging.debug('Value of toss is: ' + str(toss))
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input().lower()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
