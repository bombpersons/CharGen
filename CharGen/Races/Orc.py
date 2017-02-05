from CharGen.Character import *

class Orc:
    def __init__(self):
        pass

    def size(self, character, total):
        return Size.MEDIUM

    def str(self, character, total):
        return total + 4

    def name(self, character, total):
        return total + ["Orc"]

    def vision(self, character, total):
        return total + [Vision.NORMAL, Vision.DARK]
