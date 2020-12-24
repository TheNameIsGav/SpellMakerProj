import json
import enum

class Schools(enum.Enum):
    Death = 0
    Fire = 1
    Ice = 2
    Life = 3
    Storm = 4
    Balance = 5
    Blood = 6
    Enchantment = 7

def addEffect(schoolID, rarity, file, effect):

    school = str(Schools(schoolID))

    with open (file, 'r') as infile:
        currSpellDict = json.load(infile)

    currSpellID = currSpellDict['ID']+1

    if not school in currSpellDict.keys():
        currSpellDict[school] = []

    currSpellDict[school].append({
        'rarity': rarity,
        'effect': effect,
        'id': currSpellID
    })

    currSpellDict['ID'] = currSpellID

    with open (file, 'w') as outfile:
        json.dump(currSpellDict, outfile)


def hardReset():
    with open("data.spell", 'w') as outfile:
        json.dump({"ID": 0}, outfile)

        
def main():
    hardReset()
    addEffect(
        1,
        "rare",
        "data.spell",
        "deathcum"
    )


main()