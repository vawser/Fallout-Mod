import os
import sys
import random
import time
import colorsys

"""
Generate definition.csv with a specific color pattern for the RGB values
"""

def main():
    file = open("patterned_definition.txt", "wt")

    r = 0
    g = 0
    b = 200

    target_count = 2000

    for i in range(986, target_count):
        file.write("{id};{r};{g};{b};;;;\n".format(id=i, r=r, g=g, b=b))

        g = g + 10

        if g > 200:
            g = 100
            r = r + 5

        if r > 100:
            r = 0
            b = b + 5

    file.close()


if __name__ == "__main__":
    main()