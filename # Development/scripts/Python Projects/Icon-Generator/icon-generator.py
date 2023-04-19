import os
from pathlib import Path
from PIL import Image

SOURCE_DIR = Path( "E:\\Users\\Xylozi\\PycharmProjects\\EU4\\Icon-Generator\\input\\" )
OUTPUT_DIR = Path( "E:\\Users\\Xylozi\\PycharmProjects\\EU4\\Icon-Generator\\output\\")

def generate_icon(filename, resolution):
    file = open( OUTPUT_DIR / "output.txt", "a")
    try:
        icon = Image.open(SOURCE_DIR / filename)
        icon = icon.resize( resolution, Image.ANTIALIAS)

        a_channel = Image.new('L', resolution, 255)
        icon.putalpha(a_channel)

        icon.save( OUTPUT_DIR / "mission_icon_{0}.tga".format(filename.stem), "TGA")

        print( "Composed {0}".format(filename))

        file.write( "\tspriteType = {\n")
        file.write( "\t\tname = \"mission_icon_{0}\"\n".format(filename.stem))
        file.write("\t\ttexturefile = \"gfx//interface//missions//flags//mission_icon_{0}.tga\"\n".format(filename.stem))
        file.write("\t}\n")
        file.close()
    except:
        pass

def main():
    # 59 x 63

    for (dirpath, dirnames, filenames) in os.walk(SOURCE_DIR):
        for filename in filenames:
            generate_icon(Path(filename), ( 59, 63 ) )

if __name__ == "__main__":
    main()
