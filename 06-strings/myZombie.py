#! python3
# myZombie.py - Bots for Zombie Dice simulator game.
# Requires zombiedice package to be installed (pip install zombiedice)

import zombiedice
from random import randint

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class MyRandomZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        while diceRollResults and randint(0, 1) == 0:
            diceRollResults = zombiedice.roll()

class MyTwoBrainZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults:
            brains += diceRollResults['brains']
            if brains >= 2:
                break
            diceRollResults = zombiedice.roll()


class MyTwoShotgunZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotguns = 0
        while diceRollResults:
            shotguns += diceRollResults['shotgun']
            if shotguns >= 2:
                break
            diceRollResults = zombiedice.roll()


class MyFourThinkingZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        count = randint(1, 4)
        steps = 1
        shotguns = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults and steps < count:
            shotguns += diceRollResults['shotgun']
            if shotguns >= 2:
                break
            diceRollResults = zombiedice.roll()
            steps += 1

class MyShotgunOverBrainsZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotguns = 0
        brains = 0
        while diceRollResults:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if brains < shotguns:
                break
            diceRollResults = zombiedice.roll()


zombies = (
            MyRandomZombie(name='Random'),
            MyTwoBrainZombie(name='Stops at 2 brains'),
            MyTwoShotgunZombie(name='Stops at 2 shotguns'),
            MyFourThinkingZombie(name='Up to 4 turns'),
            MyShotgunOverBrainsZombie(name='Brains over shotguns'),
            MyZombie(name='My Zombie Bot')
        )

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
