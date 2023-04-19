import os
import xylozi_common as com
import re

"""
Add unique technological units to country file historical_unit scope
"""

country_path = "C:\\Users\\Xylozi\\Documents\\Paradox Interactive\\Europa Universalis IV\\mod\\asoiaf_test\\common\\countries\\"
history_path = "C:\\Users\\Xylozi\\Documents\\Paradox Interactive\\Europa Universalis IV\\mod\\asoiaf_test\\history\\countries\\"
tag_path = "C:\\Users\\Xylozi\\Documents\\Paradox Interactive\\Europa Universalis IV\\mod\\asoiaf_test\\common\\country_tags\\00_countries.txt"

groups = {
    "westerosi": "Westerosi",
    "essosian": "Essosian",
    "ghiscari": "Ghiscari",
    "quartheen": "Qartheen",
    "naathi": "Naathi",
    "farosi": "Farosi",
    "yiti": "Yitish",
    "hyrkooni": "Hyrkooni",
    "nefer": "Neferi",
    "stepstones": "Stepstone",
    "ibbenese": "Ibbenese",
    "summer_islanders": "Summer Islander",
    "valyrian": "Valyrian",
    "asshai": "Asshai",
    "white_walker": "White Walker",
    "bloodless": "Bloodless",
    "dothraki": "Dothraki",
    "jogos_nhai": "Jogos Nhai",
    "wildling": "Wildling",
    "mossovi": "Mossovi",
    "sothoryosi": "Sothoryosi",
    "ulthosi": "Ulthosi",
    "fishfolk": "Fishfolk",
    "shadowfolk": "Shadowfolk",
    "stonemen": "Stonemen",
    "cannibal": "Cannibal",
    "kdathi": "K'Dathi",
}

country_tags = com.get_file_as_string(tag_path)

for (dirpath, dirnames, filenames) in os.walk(history_path):
    for filename in filenames:
        name_parts = filename.split("-")
        tag = name_parts[0].rstrip()
        name = name_parts[1].rstrip().lstrip().replace(".txt", "")

        print(tag)
        print(name)

        # Get tech group
        os.chdir(history_path)
        history_file = com.get_file_as_string(filename)

        tech_match = re.search("technology_group.*(.*)", history_file)
        tech_group = tech_match.group(1)

        # Get country file name
        tag_match = re.search("{0} = \"countries/(.*).txt\"".format(tag), country_tags)
        country_file_name = tag_match.group(1)

        # Edit country file
        os.chdir(country_path)
        country_file = com.get_file_as_string(country_file_name + ".txt")

        unit_scope_match = re.search("historical_units = {.*}", country_file, re.DOTALL)

        is_present = False

        if(unit_scope_match == None):
            print("No historical_units scope present.")
        else:
            unit_scope = unit_scope_match.group()
            is_present = True
            print("Historical_units scope present.")

        tech_name = tech_group.replace("tech_", "").rstrip()

        # Add units
        country_file_data = country_file

        template = "historical_units = [\n\t{0}_inf_a_1\n\t{0}_cav_a_1\n\t{0}_inf_a_2\n\t{0}_cav_a_2\n\t{0}_inf_a_3\n\t{0}_cav_a_3\n\t{0}_inf_a_4\n\t{0}_cav_a_4\n\t{0}_inf_a_5\n\t{0}_cav_a_5\n]".format(tech_name)

        template = template.replace("[", "{")
        template = template.replace("]", "}")

        if(is_present):
            country_file_data = re.sub("historical_units = {.*}", template, country_file_data, 0, re.DOTALL)
        else:
            country_file_data = country_file_data + "\n" + template

        file = open(country_file_name + ".txt", "wt")
        file.write(country_file_data)
        file.close()

        print(country_file_name + " DONE")