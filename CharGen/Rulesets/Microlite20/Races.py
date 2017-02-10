class Human:
    def skillBonus(self, character, total):
        return total + 1

class Elf:
    def mind(self, character, total):
        return total + 2

class Dwarf:
    def str(self, character, total):
        return total + 2

class Halfling:
    def dex(self, character, total):
        return total + 2        
