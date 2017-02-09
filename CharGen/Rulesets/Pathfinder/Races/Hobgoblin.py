from CharGen.Rulesets.Pathfinder.Rules import *

class Hobgoblin:
    def __init__(self):
        pass

    def size(self, character, total):
        return "Medium"

    def speed(self, character, total):
        return 30

    def name(self, character, total):
        return total + ["Hobgoblin"]

    def vision(self, character, total):
        return total + [Vision.NORMAL] + [Vision.DARK]
