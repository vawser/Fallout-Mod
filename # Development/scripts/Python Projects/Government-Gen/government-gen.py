import xylozi_common as com
import os
from pathlib import Path

"""
Generate EU$ government files from a source CSV file
"""

def main():
    scriptDir = Path( os.getcwd() )
    sourceDir = Path( scriptDir / "source" )
    outputDir = Path ( scriptDir / "output.txt" )

    groups = get_groups_from_csv(sourceDir)

    government_template = com.get_file_as_string( sourceDir / "government_template.txt" )
    legacy_template = com.get_file_as_string(sourceDir / "legacy_template.txt")
    mechanic_template = com.get_file_as_string(sourceDir / "mechanic_template.txt")
    reform_template = com.get_file_as_string(sourceDir / "reform_template.txt")

    government_file = open( outputDir / "government.txt", "wt" )
    legacy_file = open(outputDir / "legacy.txt", "wt")
    mechanic_file = open(outputDir / "mechanic.txt", "wt")
    reform_file = open(outputDir / "reform.txt", "wt")

    loc = open( outputDir / "localization.txt", "wt")

    for group in groups:
        name = group[0]
        reform = group[1]
        desc = group[2]

        # Loc
        loc.write(" {0}: \"{1}\"\n".format(name, reform))
        loc.write(" {0}_desc: \"{1}\"\n".format(name, desc))
        loc.write(" {0}_name: \"{1}\"\n".format(name, reform))
        loc.write(" {0}_mechanic: \"{1}\"\n".format(name, reform))
        loc.write(" {0}_mechanic_desc: \"{1}\"\n".format(name, desc))
        loc.write(" {0}_legacy: \"{1}\"\n".format(name, reform))
        loc.write(" {0}_legacy_desc: \"{1}\"\n".format(name, desc))
        loc.write(" government_form_{0}: \"Government Form\"\n".format(name))
        loc.write(" bureaucracy_{0}: \"Bureaucracy\"\n".format(name))
        loc.write(" court_{0}: \"Court\"\n".format(name))
        loc.write(" rule_of_law_{0}: \"Rule of Law\"\n".format(name))
        loc.write(" justice_{0}: \"Justice\"\n".format(name))
        loc.write(" ambitions_{0}: \"Ambitions\"\n".format(name))
        loc.write("\n")

        # Government
        rgb = "{0} {1} {2}".format(com.get_random_number(0,255),
                                   com.get_random_number(0,255),
                                   com.get_random_number(0,255))

        government_contents = government_template.format(name=name, rgb=rgb, title=reform)
        government_contents = government_contents.replace("[", "{")
        government_contents = government_contents.replace("]", "}")
        government_file.write( government_contents )
        government_file.write("\n")

        # Legacy
        legacy_contents = legacy_template.format(name=name, title=reform)
        legacy_contents = legacy_contents.replace("[", "{")
        legacy_contents = legacy_contents.replace("]", "}")
        legacy_file.write(legacy_contents)
        legacy_file.write("\n")

        # Mechanics
        mechanic_contents = mechanic_template.format(name=name, title=reform)
        mechanic_contents = mechanic_contents.replace("[", "{")
        mechanic_contents = mechanic_contents.replace("]", "}")
        mechanic_file.write(mechanic_contents)
        mechanic_file.write("\n")

        # Reforms
        reform_contents = reform_template.format(name=name, title=reform)
        reform_contents = reform_contents.replace("[", "{")
        reform_contents = reform_contents.replace("]", "}")
        reform_file.write(reform_contents)
        reform_file.write("\n")

    government_file.close()
    legacy_file.close()
    mechanic_file.close()
    reform_file.close()
    loc.close()

def get_groups_from_csv( sourceDir ):
    data = com.get_csv_list( sourceDir / "groups.csv" )
    return data

if __name__ == "__main__":
    main()