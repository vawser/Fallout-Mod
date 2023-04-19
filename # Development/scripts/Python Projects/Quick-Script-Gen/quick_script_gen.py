# "C:\Program Files (x86)\Python_3_5_1\Python.exe" "C:\Users\Xylozi\Documents\Python\Projects\EU4\Quick Gen\quick_gen.py"

import os
import sys
import random
import time
import colorsys
import xylozi_common as com


def getScriptPath():
    """ Returns current path of script """
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def main():
    os.chdir(getScriptPath())

    input_list = com.get_csv_list("input.txt", ";")[0]
    template_file = com.get_file_as_string("template.txt")

    outputFile = open("mod_output.txt", "wt")

    x = 1

    for entry in input_list:
        new_entry = template_file.format(num=x, personality=entry)
        outputFile.write(new_entry)
        x = x + 1

    outputFile.close()


if __name__ == "__main__":
    main()
