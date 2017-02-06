from CharGen.Rulesets.Pathfinder.Rules import *

class DokuWikiFormatter:
    def __init__(self):
        pass

    def write(self, character):
        output = ""

        # First the name of the character.
        output = "===== " + " ".join(character.func("name")) + " =====\n"
        output += getSizeString(character.func("size")) + " " + character.func("type") + "\n\n"
        output += "**Init** " + str(character.func("init")) + "\n\n" #""; **Perception** " + str(character.func("perception")) + "\n\n"

        output += "==== DEFENSES ====\n"
        output += "**AC** " + str(getAC(character)) + ", touch " + str(getTouchAC(character)) + ", flat-footed " + str(getFlatAC(character)) + "\n\n"
        output += "**hp** " + str(getAverageHP(character)) + " (" + getHDString(character) + ")\n\n"
        output += "**Fort** " + intToBonusString(character.func("fortSave")) + ", **Ref** " + intToBonusString(character.func("refSave")) + ", **Will** " + intToBonusString(character.func("willSave")) + "\n\n"

        output += "==== OFFENSES ====\n"
        output += "**Speed** " + str(character.func("speed")) + " ft.\n\n"

        melee = character.func("melee")
        if len(melee) > 0:
            output += "**Melee** "
            for i in range(0, len(melee)):
                if i != 0:
                    output += ", "
                output += str(melee[i])
            output += "\n\n"

        ranged = character.func("ranged")
        if len(ranged) > 0:
            output += "**Ranged** "
            for i in range(0, len(ranged)):
                if i != 0:
                    output += ", "
                output += str(ranged[i])
            output += "\n\n"

        output += "==== STATISTICS ====\n"
        output += "**Str** " + str(character.func("str")) + \
                  ", **Dex** " + str(character.func("dex")) + \
                  ", **Con** " + str(character.func("con")) + \
                  ", **Int** " + str(character.func("int")) + \
                  ", **Wis** " + str(character.func("wis")) + \
                  ", **Cha** " + str(character.func("cha")) + "\n\n"
        output += "**Base Atk** " + str(character.func("BAB")) + "; **CMB** " + str(getCMB(character)) + "; **CMD** " + str(getCMD(character)) + "\n\n"
        #output += "**Feats** " ???

        skills = character.func("skills")
        if len(skills) > 0:
            output += "**Skills** "
            i = 0
            for s in skills.keys():
                if i != 0:
                    output += ", "

                skill = skills[s]
                output += "**" + s + "** " + intToBonusString(getSkillBonus(character, s))
                i += 1
            output += "\n\n"

        #output += "**Languages** " ???
        #output += "**Gear**" ???

        abilities = character.func("abilities")
        if len(abilities) > 0:
            output += "==== SPECIAL ABILITIES ====\n"
        for ability in abilities:
            output += "=== " + ability.name + " ===\n"
            output += ability.desc + "\n\n"
        return output
