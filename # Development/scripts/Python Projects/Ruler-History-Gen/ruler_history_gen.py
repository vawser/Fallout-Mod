import xylozi_common as com
import os
from pathlib import Path
import re
import random

def clean_names(d):
    t = re.sub("\s{2,200}", " ", d)
    k = t.split("\" \"")

    # Using spaces rather than quotes
    if len(k) < 2:
        k = t.split( " " )
        k = list(filter(None, k))

    l = []

    for n in k:
        n = re.sub("\"", "", n)
        n = n.lstrip()
        n = n.rstrip()
        l.append(n)

    return l

def main():
    data_folder = Path("source")
    history_template = com.get_file_as_string(data_folder / "history_template.txt")

    culture = "corsairs"
    dynasty_fixed = "Cork"

    # Get names
    male_names, female_names, surnames = get_culture_info(culture, data_folder / "cultures")

    male_ls = clean_names(male_names)
    female_ls = clean_names(female_names)
    surname_ls = clean_names(surnames)

    # Edit history
    history_file = open("output.txt", "wt")

    file_contents = history_template.format(
        name = "\"{0}\"".format(male_ls[com.get_random_number(0,len(male_ls)-1)]),
        #dynasty = "\"{0}\"".format(surname_ls[com.get_random_number(0,len(surname_ls)-1)]),
        dynasty = "\"{0}\"".format(dynasty_fixed),
        adm = com.get_random_number(0,7),
        dip = com.get_random_number(0,7),
        mil = com.get_random_number(0,7),
        age = 100 - com.get_random_number(18,60),

        name2="\"{0}\"".format(male_ls[com.get_random_number(0, len(male_ls) - 1)]),
        dynasty2="\"{0}\"".format(dynasty_fixed),
        adm2=com.get_random_number(0, 7),
        dip2=com.get_random_number(0, 7),
        mil2=com.get_random_number(0, 7),
        age2=106 - com.get_random_number(18, 60),

        name3="\"{0}\"".format(male_ls[com.get_random_number(0, len(male_ls) - 1)]),
        dynasty3="\"{0}\"".format(dynasty_fixed),
        adm3=com.get_random_number(0, 7),
        dip3=com.get_random_number(0, 7),
        mil3=com.get_random_number(0, 7),
        age3=129 - com.get_random_number(18, 60),

        name4="\"{0}\"".format(male_ls[com.get_random_number(0, len(male_ls) - 1)]),
        dynasty4="\"{0}\"".format(dynasty_fixed),
        adm4=com.get_random_number(0, 7),
        dip4=com.get_random_number(0, 7),
        mil4=com.get_random_number(0, 7),
        age4=157 - com.get_random_number(18, 60),

        name5="\"{0}\"".format(male_ls[com.get_random_number(0, len(male_ls) - 1)]),
        dynasty5="\"{0}\"".format(dynasty_fixed),
        adm5=com.get_random_number(0, 7),
        dip5=com.get_random_number(0, 7),
        mil5=com.get_random_number(0, 7),
        age5=196 - com.get_random_number(18, 60),

        name6="\"{0}\"".format(male_ls[com.get_random_number(0, len(male_ls) - 1)]),
        dynasty6="\"{0}\"".format(dynasty_fixed),
        adm6=com.get_random_number(0, 7),
        dip6=com.get_random_number(0, 7),
        mil6=com.get_random_number(0, 7),
        age6=211 - com.get_random_number(18, 60),

        name7="\"{0}\"".format(male_ls[com.get_random_number(0, len(male_ls) - 1)]),
        dynasty7="\"{0}\"".format(dynasty_fixed),
        adm7=com.get_random_number(0, 7),
        dip7=com.get_random_number(0, 7),
        mil7=com.get_random_number(0, 7),
        age7=260 - com.get_random_number(18, 60),

        name8="\"{0}\"".format(male_ls[com.get_random_number(0, len(male_ls) - 1)]),
        dynasty8="\"{0}\"".format(dynasty_fixed),
        adm8=com.get_random_number(0, 7),
        dip8=com.get_random_number(0, 7),
        mil8=com.get_random_number(0, 7),
        age8=282 - com.get_random_number(18, 60),

        name9="\"{0}\"".format(male_ls[com.get_random_number(0, len(male_ls) - 1)]),
        dynasty9="\"{0}\"".format(dynasty_fixed),
        adm9=com.get_random_number(0, 7),
        dip9=com.get_random_number(0, 7),
        mil9=com.get_random_number(0, 7),
        age9=289 - com.get_random_number(18, 60),

        name10="\"{0}\"".format(male_ls[com.get_random_number(0, len(male_ls) - 1)]),
        dynasty10="\"{0}\"".format(dynasty_fixed),
        adm10=com.get_random_number(0, 7),
        dip10=com.get_random_number(0, 7),
        mil10=com.get_random_number(0, 7),
        age10=298 - com.get_random_number(18, 60),

        name11="\"{0}\"".format(male_ls[com.get_random_number(0, len(male_ls) - 1)]),
        dynasty11="\"{0}\"".format(dynasty_fixed),
        adm11=com.get_random_number(0, 7),
        dip11=com.get_random_number(0, 7),
        mil11=com.get_random_number(0, 7),
        age11 = 304 - com.get_random_number(18, 60),
    )
    file_contents = file_contents.replace("[", "{")
    file_contents = file_contents.replace("]", "}")

    history_file.write(file_contents)
    history_file.close()

def get_culture_info(culture, cultures_folder):
    regex_string = culture + " = \{.*?male_names = \{(.*?)\}.*?female_names = \{(.*?)\}.*?dynasty_names = \{(.*?)\}.*?\}"

    gfx = ""
    male_names = ""
    female_names = ""
    surnames = ""

    for (dirpath, dirnames, filenames) in os.walk(cultures_folder):
        for filename in filenames:
            contents = com.get_file_as_string(cultures_folder / filename)

            info = re.search( regex_string, contents, flags=re.DOTALL)
            if info is not None:
                # Get names
                male_names = info.group(1)
                female_names = info.group(2)
                surnames = info.group(3)

    return male_names, female_names, surnames

if __name__ == "__main__":
    main()
