# Coin Flip Streaks
import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Create a list of 100 'heads' or 'tails' values.
    coinFlip = [None] * 100
    for i in range(100):
        if random.randint(0, 1) == 0:
            coinFlip[i] = 'H'
        else:
            coinFlip[i] = 'T'

    # Check if there is a streak of 6 heads or tails in a row.
    # One method would be to convert to a string and just look for one of the occurences
    # to be there like such:
    # coinFlip = ''.join(coinFlip)
    # if 'HHHHHH' in coinFlip or 'TTTTTT' in coinFlip:
    #    numberOfStreaks += 1

    # But a better way is to just count the streak and break early
    currentCoin = None
    streakCount = 0
    for coin in coinFlip:
        if currentCoin == None or currentCoin == coin:
            streakCount += 1
            currentCoin = coin
        else:
            streakCount = 1
            currentCoin = coin
        if streakCount == 6:
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
