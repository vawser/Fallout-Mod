import os
import os
import xylozi_common as com
import random

start_id = 1
end_id = 1037

template = com.get_file_as_string("template.txt")

os.chdir("C:\\Users\\Xylozi\\Documents\\Paradox Interactive\\Europa Universalis IV\\mod\\crimson_luna\\history\\provinces\\")

for x in range(start_id, end_id):
    outputFile = open("{0} - Province.txt".format(x), "wt")
    outputFile.write(template.format(random.randrange(1,10), random.randrange(1,10), random.randrange(1,10)))
    outputFile.close()