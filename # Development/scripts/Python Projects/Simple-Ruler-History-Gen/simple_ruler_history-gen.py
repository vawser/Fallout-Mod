# "C:\Program Files (x86)\Python_3_5_1\Python.exe" "C:\Users\Xylozi\Documents\Python\Projects\EU4\Republic History Gen\republic_history_gen.py"

import os
import sys
import random
import time


def getRandomNumber(min, max):
    return random.randrange(min, max)


def getScriptPath():
    """ Returns current path of script """
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def getRandomEntry(list):
    """Returns a random entry within the passed list"""
    return list[random.randint(0, len(list) - 1)]


def getRandomGender():
    rand = random.randrange(0, 100)
    if (rand < 75):
        return "male"
    else:
        return "female"

def getRandomHeir():
    rand = random.randrange(0, 100)
    rand2 = random.randrange(0, 100)

    female = False
    heir = True

    if (rand2 < 25):
        female = False

    if (rand < 25):
        heir = False

    return heir, female

def getBirthDate(date):
    year = date.split(".")[0]
    birthYear = int(year) - random.randrange(18, 90)
    birthYear = str(birthYear) + ".1.1"
    return birthYear


def getDeathDate(date):
    year = date.split(".")[0]
    deathYear = int(year) + random.randrange(18, 90)
    deathYear = str(deathYear) + ".1.1"
    return deathYear


def getNames(file):
    """Returns a list containing all the names found in the passed file, with newlines stripped"""
    tempList = []
    filepath = getScriptPath() + "/" + file

    with open(filepath, "rt") as sourceFile:
        text = sourceFile.readlines()

    for i in range(len(text)):
        tempList.append(text[i].strip("\n"))

    return tempList


def writeRuler(file, name, birth_date, adm, dip, mil, date, gender, dynasty):
    """Writes the monarch script code to a file"""
    file.write(date + " = {\n")
    file.write("\t" + "monarch = {\n")
    file.write("\t\t" + "name = \"" + name + "\"\n")
    file.write("\t\t" + "dynasty = \"" + dynasty + "\"\n")
    file.write("\t\t" + "birth_date = " + birth_date + "\n")
    file.write("\t\t" + "adm = " + str(adm) + "\n")
    file.write("\t\t" + "dip = " + str(dip) + "\n")
    file.write("\t\t" + "mil = " + str(mil) + "\n")

    if gender == "female":
        file.write("\t\t" + "female = yes\n")

    file.write("\t}\n")

def writeHeir(file, name, birth_date, adm, dip, mil, date, gender, dynasty, death_date):
    """Writes the monarch script code to a file"""
    file.write("\t" + "heir = {\n")
    file.write("\t\t" + "monarch_name = \"" + name + "\"\n")
    file.write("\t\t" + "name = \"" + name + "\"\n")
    file.write("\t\t" + "dynasty = \"" + dynasty + "\"\n")
    file.write("\t\t" + "birth_date = " + birth_date + "\n")
    file.write("\t\t" + "death_date = " + death_date + "\n")
    file.write("\t\t" + "adm = " + str(adm) + "\n")
    file.write("\t\t" + "dip = " + str(dip) + "\n")
    file.write("\t\t" + "mil = " + str(mil) + "\n")
    file.write("\t\t" + "claim = 100\n")

    if gender == "female":
        file.write("\t\t" + "female = yes\n")

    file.write("\t}\n")

def main():
    script_path = getScriptPath()

    dates = ["2750.1.1", "2800.1.1", "2850.1.1", "2900.1.1", "2950.1.1", "3000.1.1" ]

    maleNames = getNames("male_forenames.txt")
    femaleNames = getNames("female_forenames.txt")
    dynastyNames = getNames("dynasty_names.txt")

    dynasty = getRandomEntry(dynastyNames)

    os.chdir(script_path)

    output = open("output.txt", "w+")

    for j in range(len(dates)):
        currentDate = dates[j]

        gender = getRandomGender()
        has_heir, is_female_heir = getRandomHeir()

        if gender == "male":
            writeRuler(output, getRandomEntry(maleNames), getBirthDate(currentDate), getRandomNumber(0, 6),
                              getRandomNumber(0, 6), getRandomNumber(0, 6), currentDate, gender, dynasty)
        else:
            writeRuler(output, getRandomEntry(femaleNames), getBirthDate(currentDate), getRandomNumber(0, 6),
                              getRandomNumber(0, 6), getRandomNumber(0, 6), currentDate, gender, dynasty)

        if has_heir:
            birth_date = getBirthDate(currentDate)
            death_date = getDeathDate(birth_date)

            if is_female_heir:
                writeHeir(output, getRandomEntry(maleNames), birth_date, getRandomNumber(0, 6),
                       getRandomNumber(0, 6), getRandomNumber(0, 6), currentDate, "female", dynasty, death_date)
            else:
                writeHeir(output, getRandomEntry(femaleNames), birth_date, getRandomNumber(0, 6),
                          getRandomNumber(0, 6), getRandomNumber(0, 6), currentDate, "male", dynasty, death_date)

        # Close date bracket
        output.write("}\n\n")

    output.close()

if __name__ == "__main__":
    main()

