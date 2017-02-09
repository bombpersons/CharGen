from CharGen.Rulesets.Pathfinder.Rules import *

import random

class Human:
    def __init__(self):
        self.abilityBuff = ""

    def randomize(self):
        scores = ["str", "dex", "con", "int", "wis", "cha"]
        self.abilityBuff = random.randint(0, len(scores) - 1)

    def size(self, character, total):
        return "Medium"

    def speed(self, character, total):
        return 30

    def name(self, character, total):
        return total + ["Human"]

    def vision(self, character, total):
        return total + [Vision.NORMAL]

    def str(self, character, total):
        if self.abilityBuff == "str":
            return total + 2
        return total
    def dex(self, character, total):
        if self.abilityBuff == "dex":
            return total + 2
        return total
    def con(self, character, total):
        if self.abilityBuff == "con":
            return total + 2
        return total
    def int(self, character, total):
        if self.abilityBuff == "int":
            return total + 2
        return total
    def wis(self, character, total):
        if self.abilityBuff == "wis":
            return total + 2
        return total
    def cha(self, character, total):
        if self.abilityBuff == "cha":
            return total + 2
        return total
