def convHitDiceToString(hitdice, extra):
    s = str(hitdice[0]) + "d" + str(hitdice[1])
    if extra < 0:
        s += "-" + str(extra)
    elif extra > 0:
        s += "+" + str(extra)
    return s

def convNumToBonusString(num):
    if num == 0:
        return "0"
    elif num < 0:
        return "-" + str(abs(num))
    elif num > 0:
        return "+" + str(num)

def WriteSimple(character):
    s = ""

    s += character.getName() + "\n"
    s += "STR : " + str(character.getStat("str")) + " (" + str(character.getStatBonus("str")) + ") "
    s += "DEX : " + str(character.getStat("dex")) + " (" + str(character.getStatBonus("dex")) + ") "
    s += "MIND : " + str(character.getStat("mind")) + " (" + str(character.getStatBonus("str")) + ") \n"
    s += "HD " + convHitDiceToString(character.getHitDice(), character.getHitPointBonus()) + " (" + str(character.getHitPointAverage()) + ")\n"

    s += "AC: " 
    s += "Spell DC: " + str(character.getSpellDC()) + "\n"
    s += "Skills: "
    s += "Physical " + convNumToBonusString(character.getSkill("physical"))
    s += ", Subterfuge " + convNumToBonusString(character.getSkill("subterfuge"))
    s += ", Knowledge " + convNumToBonusString(character.getSkill("knowledge"))
    s += ", Communication " + convNumToBonusString(character.getSkill("communication"))
    s += ", Survival " + convNumToBonusString(character.getSkill("survival")) + " "

    #s += "AC "
    #s += "WEAPONS"

    abilities = character.getAbilities()
    if len(abilities) > 0:
        s += "Abilities: \n"
        for ability in abilities:
            s += ability[0] + " - " + ability[1]
        s += "\n"

    return s
