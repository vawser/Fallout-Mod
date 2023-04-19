import os
import sys
import random
import time
import colorsys

def main():
    file = open("generated_list.txt", "wt")

    start = 989
    end = 1109

    for i in range(start, end):
        file.write("{id} ".format(id=i))

    file.close()

if __name__ == "__main__":
    main()