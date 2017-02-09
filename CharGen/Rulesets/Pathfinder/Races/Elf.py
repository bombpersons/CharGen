from CharGen.Rulesets.Pathfinder.Rules import *

class Elf:
    def __init__(self):
        pass

    def size(self, character, total):
        return "Medium"

    def speed(self, character, total):
        return 30

    def name(self, character, total):
        return total + ["Elf"]

    def vision(self, character, total):
        return total + [Vision.NORMAL] + [Vision.LOW_LIGHT]

    def abilities(self, character, total):
        new = Ability("Elven Immunity", "Elves are immune to any sleep effect.")
        return total + [new]
