from CharGen.Rulesets.Pathfinder.Rules import *

class Orc:
    def __init__(self):
        pass

    def size(self, character, total):
        return "Medium"

    def speed(self, character, total):
        return 30

    def str(self, character, total):
        return total + 4

    def name(self, character, total):
        return total + ["Orc"]

    def vision(self, character, total):
        return total + [Vision.NORMAL, Vision.DARK]
