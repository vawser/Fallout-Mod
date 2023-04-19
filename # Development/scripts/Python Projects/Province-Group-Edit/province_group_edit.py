import os
import xylozi_common as com

province_dir = "C:\\Users\\Xylozi\Documents\Paradox Interactive\\Europa Universalis IV\\mod\\WWU-Old\\history\\provinces\\"

template = com.get_file_as_string("list.txt")

province_ids = template.split("\n")

os.chdir(province_dir)

for (dirpath, dirnames, filenames) in os.walk(province_dir):
    for filename in filenames:
        id = filename.split(" - ")[0]
        file_contents = com.get_file_as_string(filename)

        if id in province_ids:

            if "culture = culture_pandaren" in file_contents:
                print("Edited Province into HRE: " + id)
                file = open(filename, "wt")
                file_contents = file_contents.replace("hre = no", "hre = yes")
                file.write(file_contents)
                file.close()
            else:
                print("Edited Province out of HRE: " + id)
                file = open(filename, "wt")
                file_contents = file_contents.replace("hre = yes", "hre = no")
                file.write(file_contents)
                file.close()
