import xylozi_common as com
import os
from pathlib import Path

def main():
    generate_asset_file()

def generate_advisor_file():
    sourceDir = Path(os.getcwd())
    outputDir = sourceDir / "output.txt"

    advisors = com.get_csv_list("advisors.txt")
    groups = com.get_csv_list("gfx_cultures.txt")

    template = com.get_file_as_string("advisor_template.txt")

    genders = [ "male", "female"]

    for group in groups:
        group = group[0]
        folder_name = group.replace( "_gfx", "")

        file = open(outputDir / "zzz_{0}_advisors.gfx".format(folder_name), "wt")
        file.write("spriteTypes = {\n")

        for gender in genders:
            file.write("\t#------------------\n")
            file.write("\t# {0}\n".format(gender.title()))
            file.write("\t#------------------\n")
            for advisor in advisors:
                advisor = advisor[0]

                if gender == "female":
                    gender_part = "_female"
                else:
                    gender_part = ""

                contents = template.format(group=group, name=advisor,
                                           gender_part=gender_part, folder = folder_name, gender=gender)
                contents = contents.replace("[", "{")
                contents = contents.replace("]", "}")
                file.write(contents)
                file.write("\n")

        file.write("}")
        file.close()

def generate_asset_file():
    sourceDir = Path(os.getcwd())
    outputDir = sourceDir / "output.txt"

    groups = com.get_file_as_string("gfx_cultures.txt")
    groups = groups.split( "\n" )

    template = com.get_file_as_string("idea_template.txt")

    for line in groups:
        line = line.rstrip()
        name = line.replace( "gfx", "" )
        name = name.replace("_", " ")

        parts = name.split( " " )

        if len(parts) > 1:
            name = ""
            for idx, part in enumerate(parts):
                if idx == len(parts) - 1:
                    name = name + part.title()
                else:
                    name = name + " " + part.title()
        else:
            name = name.title()

        file = open(outputDir / "GFX - {0}.asset".format(name), "wt")

        contents = template.format(line)
        contents = contents.replace("[", "{")
        contents = contents.replace("]", "}")
        file.write(contents)
        file.write("\n")

    file.close()

if __name__ == "__main__":
    main()