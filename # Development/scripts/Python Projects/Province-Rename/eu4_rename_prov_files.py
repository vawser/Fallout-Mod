import sys
import unicodedata
import re
import os
import string
from unidecode import unidecode

#def strip_accents(s):
    #return ''.join(c for c in unicodedata.normalize('NFD', s)
    #               if unicodedata.category(c) != 'Mn')
    #return ''.join(c for c in unicodedata.normalize('NFD', s))
# don't try and normalize yourself, worst mistake of my life, just use unidecode

if len(sys.argv) != 2:
    print("usage: eu4_rename_prov_files.py [eu4 mod root]")
    exit(1)

with open(os.path.join(sys.argv[1], "localisation", "prov_names_l_english.yml"), "r") as f:
    prov_names = f.read().split("\n")

with open(os.path.join(sys.argv[1], "map", "definition.csv"), "r") as f:
    definitions = f.read().split("\n")
    # I know there's a csv parser - I'm going to not use it :obrtroll:    

history_filenames = os.listdir(os.path.join(sys.argv[1], "history", "provinces"))

for prov in prov_names:

    if not re.match(r"PROV\d{1,4}", prov.lstrip()) or prov[0] != " " or prov.lstrip()[0] == "#": # all single space indented
        # skips the l_english, the PROV_SEA_whatever, etc, we only care about PROV<ID> where ID is 1 to 4 digits
        print(f"skipping '{prov}'")
        continue

        
    prov_id = prov.lstrip().split(" ")[0][4:]
    # take the :digit off the end
    prov_id = prov_id.split(":")[0]
        
    if prov.count('"') > 2:
        print("uh oh")
        print(prov)
        input()
        
    prov_name = re.findall(r'"([^"]*)"', prov.lstrip())[0]
    # lazy - anything between quotes
    # technically you can have multiple double quotes because the loc actually ends on the quote right before the \n
    # but provinces won't have quotes in their name (or will they?)
    
    prov_name = prov_name.replace(" ","_")
    prov_name = prov_name.replace("'", "")
    prov_name = prov_name.replace("|", "")
    prov_name = prov_name.replace(":", "")
    prov_name = prov_name.replace("&", "_")
    prov_name = prov_name.replace("-", "_")
    prov_name = prov_name.replace(".", "_")

    if prov_name == "":
        prov_name = "Blank"

    print(prov_id, prov_name)
    
    if not all(x in string.ascii_letters+"_-" for x in prov_name):
        # normalize
        normal_prov_name = unidecode(prov_name) #strip_accents(prov_name)
        # hmm, I never trust unicode normalisation
        
        normal_prov_name = normal_prov_name.replace("'", "")
        # annoying edge case, sometimes people use the fancy apostrophe
        # which becomes normal '
        
        print(f"normalizing {prov_name} to {normal_prov_name}")
        #input()
        prov_name = normal_prov_name

    # 1) is the file in history/provinces named correctly?
    correct_filename = f"{prov_id} - {prov_name}.txt"
    if not correct_filename in history_filenames:
        
        # find the file with that id at the start, rename it
        wrong_filename = [filename for filename in history_filenames if filename.startswith(prov_id+" - ") or filename == prov_id+".txt"] #another edge case
        if len(wrong_filename) < 1:
            os.chdir(os.path.join(sys.argv[1], "history", "provinces"))  # Go to province dir
            output = open(correct_filename, "wt")
            output.close()
            os.chdir(os.path.join(sys.argv[1]))
            print(f"Adding file for {prov_id}")
            continue
        if len(wrong_filename) > 1:
            print(f"wtf, multiple files for {prov_id}", wrong_filename)
            continue
            
        wrong_filename = wrong_filename[0]
        
        print(f"file '{wrong_filename}' should be '{correct_filename}', renaming")
        #input()
        os.rename(os.path.join(sys.argv[1], "history", "provinces", wrong_filename), os.path.join(sys.argv[1], "history", "provinces", correct_filename))
        # for now, to test

    for i in range(len(definitions)):
        def_id = definitions[i].split(";")[0]
        r = definitions[i].split(";")[1]
        g = definitions[i].split(";")[2]
        b = definitions[i].split(";")[3]

        if prov_id == def_id:
            definitions[i] = ";".join((def_id, r, g, b, prov_name, ";;;;;"))
            break

# write back to definitions.csv -
# (also note this is \r\n - windows newline splitting - keep that consistent)
with open(os.path.join(sys.argv[1], "map", "definition.csv"), "w") as f:
    f.write("\n".join(definitions))