import os
import sys
import random
import time
import colorsys

"""
Generate province name localization
"""

def main():
    file = open("province_names.txt", "wt")

    start = 1
    end = 2000

    for i in range(start, end):
        file.write(" PROV{id}: \"PROV{id}\"\n".format(id=i))

    file.close()

if __name__ == "__main__":
    main()