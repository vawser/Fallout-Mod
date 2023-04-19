import os
import xylozi_common as com
from PIL import Image

SCRIPT_DIR = os.getcwd()
MAP_DIR = os.getcwd() + "\\maps\\"

def write_definition_hoi4(map, start_id, type, is_coastal, terrain, continent_id):
    os.chdir(MAP_DIR)

    province_map = Image.open(map)
    colors = province_map.getcolors(100000)

    os.chdir(SCRIPT_DIR)

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

    print("Extracted definitions for {map}".format(map=map))
    return current_id

def write_definition_eu4(map, start_id):
    os.chdir(MAP_DIR)

    province_map = Image.open(map)
    colors = province_map.getcolors(100000)

    os.chdir(SCRIPT_DIR)

    definition_file = open("definition.csv".format(start_id=start_id, map=map), "a")

    current_id = start_id

    for color in colors:
        # Exclude background color
        if color[1] != (255, 255, 255):
            color = color[1]
            r = color[0]
            g = color[1]
            b = color[2]

            definition_file.write( "{id};{red};{green};{blue};LAND;\n".format(id=current_id, red=r, green=g, blue=b ) )

            current_id += 1

    definition_file.close()

    print("Extracted definitions for {map}".format(map=map))
    return current_id

def main():
    print("HOI4 Definition Extract")

    com.create_directory(MAP_DIR)

    start_id = 162

    current_id = write_definition_eu4("temp.bmp", start_id)


if __name__ == "__main__":
    main()
