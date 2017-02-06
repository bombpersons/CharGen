from CharGen.Rulesets.Pathfinder.Rules import *

class Goblin:
    def __init__(self):
        pass

    def size(self, character, total):
        return Size.SMALL

    def speed(self, character, total):
        return 30

    def name(self, character, total):
        return total + ["Goblin"]

    def vision(self, character, total):
        return total + [Vision.NORMAL] + [Vision.DARK]

    def abilities(self, character, total):
        new = Ability("Incompetent", "Goblins are naturally incompetent and critical fumble any attacks that roll a natural 1 or 2.")
        return total + [new]
