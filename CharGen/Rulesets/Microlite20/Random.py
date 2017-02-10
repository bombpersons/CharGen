import CharGen.Rulesets.Microlite20.Classes as Classes
import CharGen.Rulesets.Microlite20.Races as Races

import CharGen.Rulesets.Microlite20.WeaponList as WeaponList
import CharGen.Rulesets.Microlite20.ArmorList as ArmorList

import random

def applyRandomAppropriate(character, lvl):
    c = getRandomAppropriateClass(character, lvl)
    character.apply(c)

    melee, ranged, armor, shield = getRandomAppropriateWeaponAndArmor(character, lvl)
    if melee:
        character.apply(WeaponList.WeaponTemplate(melee))
    if ranged:
        character.apply(WeaponList.WeaponTemplate(ranged))
    if armor:
        character.apply(ArmorList.ArmorTemplate(armor))
    if shield:
        character.apply(ArmorList.ArmorTemplate(shield))

def getRandomAppropriateClass(character, lvl):
    # Classes mapping to minimum required stats for that class.
    adventurerClasses = {
        Classes.Fighter : [12, 0, 0],
        Classes.Rogue : [0, 14, 0],
        Classes.Magi : [0, 0, 14],
        Classes.Cleric : [0, 0, 14]
    }

    charStats = [
        character.getStat("str"),
        character.getStat("dex"),
        character.getStat("mind")
    ]

    # Find any classes that match.
    shortList = [Classes.Commoner]
    for c, stats in adventurerClasses.items():
        qualify = True
        for charStat, stat in list(zip(charStats, stats)):
            if charStat < stat:
                qualify = False

        if qualify:
            shortList += [c]

    # Pick one of the shortlist classes at random.
    picked = shortList[random.randint(0, len(shortList) - 1)]
    instance = picked(lvl)
    return instance

def getRandomAppropriateWeaponAndArmor(character, lvl):
    # Load a list of weapons.
    weaponList = WeaponList.WeaponList()
    weaponList.loadFromFile("CharGen/Rulesets/Microlite20/Weapons.raw")

    # If we have high dex, we probably want a light weapon for our melee.
    meleeTraits = []
    if character.getStat("dex") > character.getStat("str"):
        meleeTraits = ["Light"]
    # If we have high strength, we probably want to be using something two-handed
    elif character.getStat("str") > 16:
        meleeTraits = ["Two-Handed"]

    pickedMelee = weaponList.getRandomWeapon(meleeTraits)

    # We might also want a ranged weapon.
    pickedRanged = None
    if random.randint(0, 100) > 50:
        pickedRanged = weaponList.getRandomWeapon(["Ranged"])

    # We'll want some armor if we have any proficiencies
    armorList = ArmorList.ArmorList()
    armorList.loadFromFile("CharGen/Rulesets/Microlite20/Armor.raw")

    armorProficiency = character.getArmorProficiency()

    # If we picked a two-handed weapon, we can't pick a shield.
    if "Two-Handed" in pickedMelee.traits:
        if "Shield" in armorProficiency:
            armorProficiency.remove("Shield")

    pickedShield = None
    pickedArmor = armorList.getRandomArmor(armorProficiency)

    # If we picked a shield, pick another armor
    if pickedArmor != None:
        if "Shield" in pickedArmor.traits:
            pickedShield = pickedArmor
            if "Shield" in armorProficiency:
                armorProficiency.remove("Shield")
            pickedArmor = armorList.getRandomArmor(armorProficiency)

    return (pickedMelee, pickedRanged, pickedArmor, pickedShield)
