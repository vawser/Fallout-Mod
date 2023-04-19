import os
import xylozi_common as com

from PIL import Image

SCRIPT_DIR = os.getcwd()
IMPORT_FLAGS_BASE_DIR = os.getcwd() + "\\source\\"
EXPORT_FLAGS_BASE_DIR = os.getcwd() + "\\generated\\"
EXPORT_FLAGS_MEDIUM_DIR = os.getcwd() + "\\generated\\medium"
EXPORT_FLAGS_SMALL_DIR = os.getcwd() + "\\generated\\small"

def generate_flags(tag_data, ideology_data):
    for country in tag_data:
        tag = country[0]

        os.chdir(IMPORT_FLAGS_BASE_DIR)

        # Skip missing source flags
        try:
            flag = Image.open("{0}.tga".format(tag))

            # Resize to match HOI4 flag sizes
            large_flag = flag.resize( (82, 52), Image.ANTIALIAS )
            med_flag = flag.resize( (41, 26), Image.ANTIALIAS )
            small_flag = flag.resize( (10, 7), Image.ANTIALIAS )

            large_flag = large_flag.convert("RGBA")
            med_flag = med_flag.convert("RGBA")
            small_flag = small_flag.convert("RGBA")

            # Save different flag version
            os.chdir(EXPORT_FLAGS_BASE_DIR)
            large_flag.save("{0}.tga".format(tag), "TGA")
            os.chdir(EXPORT_FLAGS_MEDIUM_DIR)
            med_flag.save("{0}.tga".format(tag), "TGA")
            os.chdir(EXPORT_FLAGS_SMALL_DIR)
            small_flag.save("{0}.tga".format(tag), "TGA")

            for ideology in ideology_data:
                os.chdir(EXPORT_FLAGS_BASE_DIR)
                large_flag.save("{0}_{1}.tga".format(tag,ideology), "TGA")

                os.chdir(EXPORT_FLAGS_MEDIUM_DIR)
                med_flag.save("{0}_{1}.tga".format(tag,ideology), "TGA")

                os.chdir(EXPORT_FLAGS_SMALL_DIR)
                small_flag.save("{0}_{1}.tga".format(tag,ideology), "TGA")
        except:
            print( "Missing source flag for {0}".format(tag))

def main():
    print("HOI4 Flag Generator")

    # Create directories used by script

    com.create_directory(IMPORT_FLAGS_BASE_DIR)
    com.create_directory(EXPORT_FLAGS_BASE_DIR)
    com.create_directory(EXPORT_FLAGS_MEDIUM_DIR)
    com.create_directory(EXPORT_FLAGS_SMALL_DIR)

    os.chdir(SCRIPT_DIR)

    tag_data = com.get_csv_list("data.csv")
    ideology_data = [ "light", "shadow", "order", "disorder", "life", "death", "unaligned"]

    generate_flags(tag_data, ideology_data)


if __name__ == "__main__":
    main()
