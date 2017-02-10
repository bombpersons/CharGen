import CharGen.Dice as Dice

class Base:
    def __init__(self):
        self.varStr = 10
        self.varDex = 10
        self.varMind = 10

    def randomize(self):
        self.varStr = Dice.rollDice(3, 6)
        self.varDex = Dice.rollDice(3, 6)
        self.varMind = Dice.rollDice(3, 6)

    def str(self, character, total):
        return total + self.varStr

    def dex(self, character, total):
        return total + self.varDex

    def mind(self, character, total):
        return total + self.varMind
