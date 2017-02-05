from CharGen.Character import *

class Orc:
    def __init__(self):
        pass

    def str(self, character):
        return 4

    def name(self, character):
        return ["Orc"]

    def vision(self, character):
        return [Vision.NORMAL, Vision.DARK]
