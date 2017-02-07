from CharGen.Rulesets.Pathfinder.Rules import *

class DokuWikiFormatter:
    def __init__(self):
        pass

    def write(self, character):
        output = ""

        # First the name of the character.
        output = "===== " + character.getName() + " =====\n"
        output += character.getSize() + " " + character.getType() + "\n\n"
        output += "**Init** " + numToBonusString(character.getInitBonus()) + "; **Perception** " + numToBonusString(character.getSkillBonus("Perception")) + "\n\n"

        output += "==== DEFENSES ====\n"
        output += "**AC** " + str(character.getAC()) + ", touch " + str(character.getTouchAC()) + ", flat-footed " + str(character.getFlatAC()) + "\n\n"
        output += "**hp** " + str(character.getAverageHP()) + " (" + character.getHDString() + ")\n\n"
        output += "**Fort** " + numToBonusString(character.getFortSave()) + ", **Ref** " + numToBonusString(character.getFortSave()) + ", **Will** " + numToBonusString(character.getWillSave()) + "\n\n"

        output += "==== OFFENSES ====\n"
        output += "**Speed** " + str(character.getSpeed()) + " ft.\n\n"

        melee = character.getMeleeAttacks()
        if len(melee) > 0:
            output += "**Melee** "
            for i in range(0, len(melee)):
                if i != 0:
                    output += ", "
                output += str(melee[i])
            output += "\n\n"

        ranged = character.getRangedAttacks()
        if len(ranged) > 0:
            output += "**Ranged** "
            for i in range(0, len(ranged)):
                if i != 0:
                    output += ", "
                output += str(ranged[i])
            output += "\n\n"

        # Spells
        spellLists = character.getSpellLists()
        for spellListName in spellLists.keys():
            spellList = spellLists[spellListName]

            # For each spell list.
            if not spellList.isEmpty():
                output += "**" + spellListName + "**"
                output += " (CL " + str(spellList.getCasterLevel()) + "; concentration " + numToBonusString(spellList.getConcentrationBonus(character)) + ")\n\n"

                for i in range(0, 10):
                    spells = spellList.getSpells(i)
                    if len(spells) > 0:
                        output += "     " + str(i) + " Lvl"

                        # If it's a spontaneous spell list, list the number of spells per day.
                        if spellList.getSpellsPerDay(i) > 0:
                            output += " (" + str(spellList.getSpellsPerDay(i)) + "/day)"

                        # List the spell DC.
                        output += " (DC " + str(spellList.getDC(character, i)) + ") - "

                        # List the spells for this spell level.
                        i = 0
                        for spellName in spells.keys():
                            if i != 0:
                                output += ", "
                            output += spellName

                            spellCount = spells[spellName]
                            if spellCount > 1:
                                output += " x" + str(spellCount)
                            i += 1

                        output += "\n\n"

        output += "==== STATISTICS ====\n"
        output += "**Str** " + str(character.getStat("str")) + \
                  ", **Dex** " + str(character.getStat("dex")) + \
                  ", **Con** " + str(character.getStat("con")) + \
                  ", **Int** " + str(character.getStat("int")) + \
                  ", **Wis** " + str(character.getStat("wis")) + \
                  ", **Cha** " + str(character.getStat("cha")) + "\n\n"
        output += "**Base Atk** " + numToBonusString(character.getBAB()) + "; **CMB** " + numToBonusString(character.getCMB()) + "; **CMD** " + str(character.getCMD()) + "\n\n"
        #output += "**Feats** " ???

        skills = character.getSkillList()
        if len(skills) > 0:
            output += "**Skills** "
            i = 0
            for s in skills:
                if i != 0:
                    output += ", "
                output += "**" + s + "** " + numToBonusString(character.getSkillBonus(s))
                i += 1
            output += "\n\n"

        #output += "**Languages** " ???
        #output += "**Gear**" ???

        abilities = character.getAbilityList()
        if len(abilities) > 0:
            output += "==== SPECIAL ABILITIES ====\n"
        for ability in abilities:
            output += "=== " + ability.name + " ===\n"
            output += ability.desc + "\n\n"
        return output
