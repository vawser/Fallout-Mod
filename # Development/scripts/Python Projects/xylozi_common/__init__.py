import csv
import random
import os


def get_csv_list(csv_file, delimiter=";"):
    data = []

    with open(csv_file, "r") as f:
        reader = csv.reader(f, delimiter=delimiter)
        data = list(reader)

    return data


def get_file_as_string(filepath):
    with open(filepath, "rt", encoding='windows-1252') as sourceFile:
        text = sourceFile.readlines()

    text_string = ""

    for i in range(len(text)):
        text_string = text_string + text[i]

    return text_string


def get_random_number(min, max):
    return random.randrange(min, max)


def get_random_color():
    return [get_random_number(0, 255), get_random_number(0, 255), get_random_number(0, 255)]


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def random_list_value(t_list):
    return t_list[random.randint(0, len(t_list) - 1)]


def clamp(n, smallest, largest): return max(smallest, min(n, largest))


def delete_directory_contents(directory):
    for (dirpath, dirnames, filenames) in os.walk(directory):
        for filename in filenames:
            try:
                os.remove("{0}//{1}".format(directory, filename))
            except OSError:
                print("OSError")
