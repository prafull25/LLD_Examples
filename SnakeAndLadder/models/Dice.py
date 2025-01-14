import random

class Dice:
    def __init__(self,sides):
        self.sides = sides

    def roll(self):
        flip_value = random.randrange(1,self.sides +1)
        return flip_value
