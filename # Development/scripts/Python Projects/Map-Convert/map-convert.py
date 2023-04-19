import os
import xylozi_common as com
from PIL import Image
import re as re
import shutil

SCRIPT_DIR = os.getcwd()
SOURCE_DIR = os.getcwd() + "\\files\\"
CONVERT_DIR = os.getcwd() + "\\converted_files\\"


def main():
    print("Map Convert")

    os.chdir(SOURCE_DIR + "\\map\\")

    # Get used provinces from image
    province_map = Image.open("provinces.bmp")

    # id, r, g, b
    def_list = build_map_definitions(province_map)

    # id, r, g, b, old_id
    def_list = build_convert_list(def_list)

    write_convert_file(def_list)

    # Convert
    # write_new_definitions(def_list)
    #convert_province_files(def_list)
    #convert_province_names(def_list)
    #convert_id_list(def_list)
    convert_area_file(def_list)

def convert_area_file(def_list):
    os.chdir(SOURCE_DIR + "\\map\\")

    areas = com.get_file_as_string("area.txt")

    # [a-z,_]+ = \{.*?\}
    area_data = re.search("[a-z,_]+ = \{(.*?\)}", areas, flags=re.DOTALL).groups()
    print(area_data)

def convert_id_list(def_list):
    os.chdir(SCRIPT_DIR)

    id_list = com.get_file_as_string("id_list.txt")
    convert_id_list = open( "converted_id_list.txt", "wt")

    id_contents = id_list.split( " " )
    #print(id_contents)
    for id in id_contents:
        id = str(id)
        locked = False

        for entry in def_list:
            if str(entry[4]) == id and locked == False:
                convert_id_list.write(str(entry[0]))
                convert_id_list.write( " " )
                locked = True

    convert_id_list.close()

def convert_province_files(def_list):
    for root, dirs, files in os.walk(SOURCE_DIR + "\\history\\provinces\\"):
        for province_file in files:
            id = province_file.split( "-" )[0].strip()
            name = province_file.split( "-" )[1].strip()
            print(id)
            print(name)

            locked = False
            for entry in def_list:
                if str(entry[4]) == id and locked == False:
                    locked = True
                    id = str(entry[0])

            if locked:
                shutil.copy2(SOURCE_DIR + "\\history\\provinces\\" + province_file,
                         CONVERT_DIR + "\\history\\provinces\\{0} - {1}".format(id, name))


def convert_province_names(def_list):
    os.chdir(SOURCE_DIR + "\\localization\\")
    contents = com.get_file_as_string("prov_names_l_english.yml")

    os.chdir(CONVERT_DIR + "\\localization\\")

    contents = contents.split( "\n" )

    for line in contents:
        locked = False
        for entry in def_list:
            if line.find( "PROV{0}:".format(entry[4]) ) != -1 and locked == False:
                line = line.replace( "PROV{0}:".format(entry[4]), "PROV{0}:".format(entry[0]))
                locked = True

        if locked == True:
            print(line)

def write_new_definitions(def_list):
    os.chdir(CONVERT_DIR + "\\map\\")

    file = open("definition.csv", "wt")
    file.write("province;red;green;blue;x;x\n")
    for entry in def_list:
        file.write("{0};{1};{2};{3};x;x\n".format(entry[0], entry[1], entry[2], entry[3]))


def write_convert_file(def_list):
    os.chdir(SCRIPT_DIR)

    file = open("convert_list.csv", "wt")
    file.write("Old ID;New ID\n")
    for entry in def_list:
        file.write("{0};{1}\n".format(entry[4], entry[0]))


def build_convert_list(def_list):
    file = com.get_csv_list("definition.csv")

    for line in file:
        old_color = (int(line[1]), int(line[2]), int(line[3]))

        for entry in def_list:
            color = (int(entry[1]), int(entry[2]), int(entry[3]))

            if old_color == color:
                entry.append(int(line[0]))

    return def_list


def build_map_definitions(map):
    colors = map.getcolors(100000)

    def_list = []
    id = 1

    for color_tuple in colors:
        color = color_tuple[1]
        r = color[0]
        g = color[1]
        b = color[2]
        def_list.append([id, r, g, b])
        id += 1

    return def_list


def write_definitions(def_list):
    definition_file = open("definition.csv".format(start_id=start_id, map=map), "a")

    current_id = start_id

    for color in colors:
        # Exclude background color
        if color[1] != (255, 255, 255):
            color = color[1]
            r = color[0]
            g = color[1]
            b = color[2]

            definition_file.write(
                "{id};{red};{green};{blue};{type};{is_coastal};{terrain};{continent}\n".format(id=current_id, red=r,
                                                                                               green=g, blue=b,
                                                                                               type=type,
                                                                                               is_coastal=is_coastal,
                                                                                               terrain=terrain,
                                                                                               continent=continent_id))

            current_id += 1

    definition_file.close()


if __name__ == "__main__":
    main()
