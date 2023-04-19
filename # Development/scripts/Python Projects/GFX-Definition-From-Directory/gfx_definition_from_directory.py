import os
import xylozi_common as com

input_dir = "C:\\Users\\Xylozi\Documents\Paradox Interactive\\Europa Universalis IV\\mod\\WWU-Old\gfx\\event_pictures"

template = com.get_file_as_string("template.txt")

file = open("output.txt", "wt")

for (dirpath, dirnames, filenames) in os.walk(input_dir):
    current_dir = dirpath.replace(input_dir, "")
    current_dir = current_dir.replace("\\", "")

    file.write("#---------------------------------\n")
    file.write("# " + current_dir + "\n")
    file.write("#---------------------------------\n")
    file.write("")

    for filename in filenames:
        name = filename.replace(".dds", "")
        title_name = name

        print(filename)
        file.write(template.format(name=name, dir=current_dir, title_name=title_name))

file.close()