import csv, random

class Armor:
    def __init__(self, name, cost, bonus, traits):
        self.name = name
        self.cost = cost
        self.bonus = bonus
        self.traits = traits

class ArmorTemplate:
    def __init__(self, armor):
        self.armor = armor

    def acBonus(self, character, total):
        return total + self.armor.bonus

    def gear(self, character, total):
        return total + [self.armor.name]

class ArmorList:
    def __init__(self):
        self.set = {}

    def loadFromFile(self, filename):
        with open(filename, newline='') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for row in reader:
                name = row[0]
                cost = int(row[1])
                bonus = int(row[2])
                traits = row[3].split(' ')
                self.set[name] = Armor(name, cost, bonus, traits)

    def getArmor(self, name):
        return self.set[name]

    def getRandomArmor(self, traits):
        # Gather weapons that match the required traits.
        potential = self.getArmor(traits)
        if len(potential) == 0:
            return None

        # Pick one entirely at random.
        r = random.randint(0, len(potential) - 1)
        return potential[r]

    def getArmor(self, traits):
        weapons = []
        for weapon in self.set.values():
            found = True
            for trait in traits:
                if trait not in weapon.traits:
                    found = False

            if found:
                weapons += [weapon]
        return weapons
