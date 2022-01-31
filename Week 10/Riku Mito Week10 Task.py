# Week 10 Task

import random

class Dice:
    sides = 0
    numDice = 0
    rolls = 0

    def __init__(self, sides, numDice, rolls):
        self.sides = sides
        self.numDice = numDice
        self.rolls = rolls

    def rollDice(self):
        for x in range(self.rolls):
            rollList = []
            for x in range(self.numDice):
                rollList.append(random.randint(1, self.sides))
            print(rollList)

dice = Dice(20, 1, 6)
Dice.rollDice(dice)
