from CharGen.Character import *

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
        #output += "**AC** " + str(character.func("AC")) + ", " + " touch " + str(character.find("touchAC")) + ", flat-footed " + str(character.find("flatFootedAC")) + "\n\n"
        #output += "**hp** " + str(getAverageHP(character)) + " (" + getHDString(character) + ")\n\n"
        output += "**Fort** " + str(character.func("fortSave")) + ", **Ref**" + str(character.func("refSave")) + ", **Will** " + str(character.func("willSave")) + "\n\n"

        output += "==== OFFENSES ====\n"
        output += "**Speed** " + str(character.func("speed")) + " ft.\n\n"
        #output += "**Melee** " + getAttackString(character.func("melee")) + "\n\n"

        output += "==== STATISTICS ====\n"
        output += "**Str** " + str(character.func("str")) + \
                  ", **Dex** " + str(character.func("dex")) + \
                  ", **Con** " + str(character.func("con")) + \
                  ", **Int** " + str(character.func("int")) + \
                  ", **Wis** " + str(character.func("wis")) + \
                  ", **Cha** " + str(character.func("cha")) + "\n\n"
        output += "**Base Atk** " + str(character.func("BAB")) + "; **CMB** " + str(character.func("CMB")) + "; **CMD** " + str(character.func("CMD")) + "\n\n"
        #output += "**Feats** " ???
        #output += "**Skills** " ???
        #output +=  "**Languages** " ???
        #output += "**Gear**" ???

        return output
