import xylozi_common as com
import os
from pathlib import Path
import re
import random

"""
Generate EU4 country file/history file/localization from source CSV file
"""

def main():
    data_folder = Path("source")
    output_folder = Path("output.txt")

    # Override old files
    file = open(output_folder / "localization.txt", "wt")
    file.close()

    data = com.get_csv_list(data_folder / "data.csv", ",")

    for country in data:
        generate_country_file(country, data_folder, output_folder)
        generate_country_history(country, data_folder, output_folder)
        generate_country_localization(country, data_folder, output_folder)
        print("Completed: {0}".format(country[1]))


def generate_country_file(data, data_folder, output_folder):
    country_folder = output_folder / "country"
    country_template = com.get_file_as_string(data_folder / "country_template.txt")

    male_names, female_names, surnames = get_culture_info(data[3], data_folder / "cultures")

    male_ls = clean_names(male_names)
    female_ls = clean_names(female_names)
    surname_ls = clean_names(surnames)

    ship_ls = [ "Sunshatter", "Windshear", "Swiftsea", "Gleenshore", "Greengem", "Rubyshine", "Quicksilver" ]

    gfx = "humangfx"
    color = "{0} {1} {2}".format(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255) )

    monarch_names = ""
    leader_names = ""
    ship_names = ""

    for name in male_ls:
        entry = "\t\"{0} #0\" = {1}\n".format(name, 20)
        monarch_names = monarch_names + entry

    for name in female_ls:
        entry = "\t\"{0} #0\" = {1}\n".format(name, -20)
        monarch_names = monarch_names + entry

    for name in surname_ls:
        entry = "\t\"{0}\"\n".format(name)
        leader_names = leader_names + entry

    for name in ship_ls:
        entry = "\t\"{0}\"\n".format(name)
        ship_names = ship_names + entry

    file_contents = country_template.format(
        gfx = data[6],
        color = color,
        monarch_names = monarch_names,
        leader_names = leader_names,
        ship_names = ship_names
    )
    file_contents = file_contents.replace( "[", "{")
    file_contents = file_contents.replace( "]", "}")

    file = open( output_folder / "country" / "{0}.txt".format(data[1]), "wt")
    file.write(file_contents)
    file.close()

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

def generate_country_history(data, data_folder, output_folder):
    history_folder = output_folder / "history"
    history_template = com.get_file_as_string(data_folder / "history_template.txt")

    male_names, female_names, surnames = get_culture_info(data[3], data_folder / "cultures")

    male_ls = clean_names(male_names)
    female_ls = clean_names(female_names)
    surname_ls = clean_names(surnames)

    file_contents = history_template.format(
        tech_group = data[4],
        government = data[5],
        culture = data[3],
        religion = data[2],

        name = "\"{0}\"".format(male_ls[com.get_random_number(0,len(male_ls)-1)]),
        dynasty = "\"{0}\"".format(surname_ls[com.get_random_number(0,len(surname_ls)-1)]),
        adm = com.get_random_number(0,6),
        dip = com.get_random_number(0,6),
        mil = com.get_random_number(0,6),

        name2="\"{0}\"".format(male_ls[com.get_random_number(0, len(male_ls) - 1)]),
        dynasty2="\"{0}\"".format(surname_ls[com.get_random_number(0, len(surname_ls) - 1)]),
        adm2=com.get_random_number(0, 6),
        dip2=com.get_random_number(0, 6),
        mil2=com.get_random_number(0, 6),

        name3="\"{0}\"".format(male_ls[com.get_random_number(0, len(male_ls) - 1)]),
        dynasty3="\"{0}\"".format(surname_ls[com.get_random_number(0, len(surname_ls) - 1)]),
        adm3=com.get_random_number(0, 6),
        dip3=com.get_random_number(0, 6),
        mil3=com.get_random_number(0, 6),

        name4="\"{0}\"".format(male_ls[com.get_random_number(0, len(male_ls) - 1)]),
        dynasty4="\"{0}\"".format(surname_ls[com.get_random_number(0, len(surname_ls) - 1)]),
        adm4=com.get_random_number(0, 6),
        dip4=com.get_random_number(0, 6),
        mil4=com.get_random_number(0, 6),

        name5="\"{0}\"".format(male_ls[com.get_random_number(0, len(male_ls) - 1)]),
        dynasty5="\"{0}\"".format(surname_ls[com.get_random_number(0, len(surname_ls) - 1)]),
        adm5=com.get_random_number(0, 6),
        dip5=com.get_random_number(0, 6),
        mil5=com.get_random_number(0, 6)

    )
    file_contents = file_contents.replace("[", "{")
    file_contents = file_contents.replace("]", "}")

    file = open(output_folder / "history" / "{0} - {1}.txt".format(data[0], data[1]), "wt")
    file.write(file_contents)
    file.close()

def generate_country_localization(data, data_folder, output_folder):
    name = data[0]
    title = data[1]

    file = open(output_folder / "localization.txt", "a")
    file.write(" {0}: \"{1}\"\n".format(name, title))
    file.write(" {0}_ADJ: \"{1}\"\n".format(name, title))
    file.close()

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
