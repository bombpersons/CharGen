from CharGen.Rulesets.Pathfinder.Rules import *

class Dwarf:
    def __init__(self):
        pass

    def size(self, character, total):
        return "Medium"

    def speed(self, character, total):
        return 20

    def name(self, character, total):
        return total + ["Dwarf"]

    def vision(self, character, total):
        return total + [Vision.NORMAL] + [Vision.DARK]

    def abilities(self, character, total):
        new = Ability("Dwarven Stubbornness", "Dwarves are unnaffected by encumberance")
        return total + [new]
