import csv, random

def parseDmg(s):
    split = s.split('d')
    return (int(split[0]), int(split[1]))

class Weapon:
    def __init__(self, name, cost, dmg, range, traits):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.range = range
        self.traits = traits

class WeaponTemplate:
    def __init__(self, weapon):
        self.weapon = weapon

    def attacks(self, character, total):
        return total + [self.weapon]

    def gear(self, character, total):
        return total + [self.weapon.name]

class WeaponList:
    def __init__(self):
        self.set = {}

    def loadFromFile(self, filename):
        with open(filename, newline='') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for row in reader:
                name = row[0]
                cost = int(row[1])
                dmg = parseDmg(row[2])
                range = int(row[3])
                traits = row[4].split(' ')
                self.set[name] = Weapon(name, cost, dmg, range, traits)

    def getWeapon(self, name):
        return self.set[name]

    def getRandomWeapon(self, traits):
        # Gather weapons that match the required traits.
        potential = self.getWeapons(traits)
        if len(potential) == 0:
            return None

        # Pick one entirely at random.
        r = random.randint(0, len(potential) - 1)
        return potential[r]

    def getWeapons(self, traits):
        weapons = []
        for weapon in self.set.values():
            found = True
            for trait in traits:
                if trait not in weapon.traits:
                    found = False

            if found:
                weapons += [weapon]
        return weapons
