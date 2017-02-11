import CharGen.Rulesets.Pathfinder.Classes.Sorcerer as Sorcerer
import CharGen.Rulesets.Pathfinder.Classes.Wizard as Wizard
import CharGen.Rulesets.Pathfinder.Classes.Warrior as Warrior
import CharGen.Rulesets.Pathfinder.Classes.Adept as Adept
import CharGen.Rulesets.Pathfinder.Classes.Rogue as Rogue
import CharGen.Rulesets.Pathfinder.Classes.Bard as Bard

import CharGen.Rulesets.Pathfinder.Classes.Commoner as Commoner
import CharGen.Rulesets.Pathfinder.Classes.Expert as Expert
import CharGen.Rulesets.Pathfinder.Classes.Aristocrat as Aristocrat

import CharGen.Rulesets.Pathfinder.Races.Dwarf as Dwarf
import CharGen.Rulesets.Pathfinder.Races.Elf as Elf
import CharGen.Rulesets.Pathfinder.Races.Goblin as Goblin
import CharGen.Rulesets.Pathfinder.Races.Hobgoblin as Hobgoblin
import CharGen.Rulesets.Pathfinder.Races.Human as Human
import CharGen.Rulesets.Pathfinder.Races.Orc as Orc
import CharGen.Rulesets.Pathfinder.Races.Ratfolk as Ratfolk

import CharGen.Rulesets.Pathfinder.Weapons as Weapons
import CharGen.Rulesets.Pathfinder.Armor as Armor

import random

class SkillRankTemplate:
    def __init__(self, ranks):
        self.ranks = ranks

    def skills(self, character, total):
        for skill, points in self.ranks.items():
            total[skill].ranks += points
        return total

def applyRandomAppropriateClass(character, lvl):
    # Get an appropriate class.
    c = getRandomAppropriateClass(character, lvl)
    character.apply(c)

    # Get a weapon
    weapon, armor, shield = getRandomAppropriateWeaponAndArmor(character)
    if weapon != None:
        character.apply(Weapons.WeaponTemplate(weapon))
    if armor != None:
        character.apply(Armor.ArmorTemplate(armor))
    if shield != None:
        character.apply(Armor.ArmorTemplate(shield))

    # Apply some skill points.
    ranks = getRandomAppropriateSkillRanks(character)
    character.apply(SkillRankTemplate(ranks))

def getRandomRace():
    possibleRaces = [
        Dwarf.Dwarf,
        Elf.Elf,
        Goblin.Goblin,
        Hobgoblin.Hobgoblin,
        Human.Human,
        Orc.Orc,
        Ratfolk.Ratfolk
    ]

    picked = possibleRaces[random.randint(0, len(possibleRaces) - 1)]
    instance = picked()

    if "randomize" in dir(instance):
        instance.randomize()
    return instance

def getRandomAppropriateClass(character, lvl):
    # Classes, with a list of minimum stats
    possibleClasses = {
        Sorcerer.Sorcerer : [0, 0, 0, 0, 0, 14],
        Wizard.Wizard : [0, 0, 0, 14, 0, 0],
        Warrior.Warrior : [12, 5, 5, 0, 0, 0],
        Adept.Adept : [0, 0, 0, 0, 14, 0],
        Rogue.Rogue : [0, 14, 0, 0, 0, 0],
        Bard.Bard : [0, 0, 0, 0, 0, 14]
    }

    commonerClasses = [
        #Commoner.Commoner,
        #Expert.Expert,
        Aristocrat.Aristocrat
    ]

    # Get the character stats
    charStats = [
        character.getStat("str"),
        character.getStat("dex"),
        character.getStat("con"),
        character.getStat("int"),
        character.getStat("wis"),
        character.getStat("cha")
    ]

    # Figure out the best class for them.
    shortList = commonerClasses
    for c, stats in possibleClasses.items():
        qualify = True
        for charStat, stat in list(zip(charStats, stats)):
            if charStat < stat:
                qualify = False

        if qualify:
            shortList += [c]

    # Pick one of the shortlist classes at random.
    picked = shortList[random.randint(0, len(shortList) - 1)]
    instance = picked(lvl)
    if "randomize" in dir(instance):
        instance.randomize(character)
    return instance

def getRandomAppropriateWeaponAndArmor(character):
    # Get our weapon proficiencies
    weapons = character.getWeaponProficiencies()
    weaponTraits = character.getWeaponTraitProficiencies()

    # Get a list of all weapons.
    allWeapons = Weapons.WeaponList()

    # List all of the weapons that have any of the traits we have.
    possibleWeapons = []
    for trait in weaponTraits:
        possibleWeapons += allWeapons.getWeapons([trait])

    for weapon in weapons:
        possibleWeapons += [allWeapons.getWeapon(weapon)]

    # Pick one at random.
    pickedWeapon = None
    if len(possibleWeapons) != 0:
        pickedWeapon = possibleWeapons[random.randint(0, len(possibleWeapons) - 1)]

    # Get our armor Proficiencies
    armorTraits = character.getArmorTraitProficiencies()

    # Get a list of all armors.
    allArmors = Armor.ArmorList()

    # List all possible armors that have any of the traits we have.
    possibleArmor = []
    for trait in armorTraits:
        # If we picked a two handed weapon, then don't pick any shields.
        if pickedWeapon != None:
            if "Two-Handed" in pickedWeapon.traits and trait == "Shield":
                continue

        possibleArmor += allArmors.getArmors([trait])

    # Pick something.
    pickedArmor = None
    pickedShield = None
    if len(possibleArmor) > 0:
        while not pickedArmor:
            picked = possibleArmor[random.randint(0, len(possibleArmor) - 1)]
            if "Shield" in picked.traits:
                pickedShield = picked
            else:
                pickedArmor = picked

    return (pickedWeapon, pickedArmor, pickedShield)

def getRandomAppropriateSkillRanks(character):
    # Get how many skill ranks we have.
    skillRanks = character.getSkillRanks()

    # For now, assign them randomly =/
    skills = character.getSkillList()
    ranks = {}
    for i in range(1, skillRanks):
        randomSkill = skills[random.randint(0, len(skills) - 1)]
        if randomSkill not in ranks:
            ranks[randomSkill] = 1
        else:
            ranks[randomSkill] += 1

    return ranks
