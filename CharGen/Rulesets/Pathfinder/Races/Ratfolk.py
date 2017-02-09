from CharGen.Rulesets.Pathfinder.Rules import *

class Ratfolk:
    def __init__(self):
        pass

    def size(self, character, total):
        return "Small"

    def speed(self, character, total):
        return 20

    def name(self, character, total):
        return total + ["Ratfolk"]

    def vision(self, character, total):
        return total + [Vision.NORMAL] + [Vision.DARK]

    def abilities(self, character, total):
        new = Ability("Resistant", "Ratfolk are unusually resistant to poisons and diseases, giving them a +2 to any save relating to it.")
        return total + [new]
