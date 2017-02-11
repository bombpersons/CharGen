from CharGen.Rulesets.Pathfinder.Rules import *

class Grippli:
    def __init__(self):
        pass

    def size(self, character, total):
        return "Small"

    def speed(self, character, total):
        return 30

    def name(self, character, total):
        return total + ["Grippli"]

    def vision(self, character, total):
        return total + [Vision.NORMAL] + [Vision.DARK]
