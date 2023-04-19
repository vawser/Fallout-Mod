import os

start_id = 1
end_id = 5000

os.chdir("C:\\Users\\Xylozi\\Documents\\Paradox Interactive\\Europa Universalis IV\\mod\\debug_mod\\history\\provinces\\")

for x in range(start_id, end_id):
    outputFile = open("{0} - Province.txt".format(x), "wt")
    outputFile.close()