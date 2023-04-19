import os
import xylozi_common as com
from PIL import Image

SCRIPT_DIR = os.getcwd()
ICON_DIR = "C:\\Users\\Xylozi\\PycharmProjects\\HOI4\\Icon-Generator\\icons"
EXPORT_DIR = "C:\\Users\\Xylozi\\PycharmProjects\\HOI4\\Icon-Generator\\export"
TEMPLATE_DIR = os.getcwd() + "\\templates\\"

def generate_icon(template, background, alpha, icon, input_offset, output_offset, input_size, output_size):
    name = icon.split( "." )[0].lower()

    os.chdir(TEMPLATE_DIR)
    template = Image.open(template)
    bg = Image.open(background)
    alpha = Image.open(alpha).convert("L")

    template = template.resize((int(input_size[0]+(input_offset[0]*2)), int(input_size[1]+(input_offset[1]*2))), Image.ANTIALIAS)
    bg = bg.resize((int(input_size[0]+(input_offset[0]*2)), int(input_size[1]+(input_offset[1]*2))), Image.ANTIALIAS)
    alpha = alpha.resize((int(input_size[0]+(input_offset[0]*2)), int(input_size[1]+(input_offset[1]*2))), Image.ANTIALIAS)

    os.chdir(ICON_DIR)
    icon = Image.open(icon)
    icon = icon.resize((int(output_size[0]), int(output_size[1])), Image.ANTIALIAS)
    icon_alpha = alpha.resize((int(output_size[0]), int(output_size[1])), Image.ANTIALIAS)

    composite = bg
    composite.paste(icon, (output_offset[0],output_offset[1]), icon_alpha)
    composite.paste(template, (0, 0), template)
    composite.putalpha(alpha)   # Adds alpha channel

    os.chdir(EXPORT_DIR)
    composite.save("{0}.tga".format(name), "TGA")

    print( "Composed {0}".format(name))

def delete_icons():
    os.chdir(SCRIPT_DIR)
    for (dirpath, dirnames, filenames) in os.walk(EXPORT_DIR):
        for filename in filenames:
            try:
                os.remove( "{0}//{1}".format(EXPORT_DIR, filename) )
            except OSError:
                print( "OSError" )

def main():
    print("HOI4 Icon Generator")

    # Clean up old icons
    #delete_icons()
    #output_file = open("output.txt", "wt")
    #output_file.close()

    # Generate icons from each source icon
    template = "eu4_mission_42x42.png"
    background = "background.png"
    alpha_bg = "eu4_mission_42x42_alpha.png"

    # Resultant Icon
    input_size = [42, 42]
    input_offset = [0, 0]

    # WoW Icon
    output_size = [50, 50]
    output_offset = [-3 , -3]

    for (dirpath, dirnames, filenames) in os.walk(ICON_DIR):
        for filename in filenames:
            # Circle
            generate_icon(template, background, alpha_bg, filename, input_offset, output_offset, input_size, output_size)

if __name__ == "__main__":
    main()
