import xylozi_common as com
import os

"""
Generate EU4 advisor GFX definitions for WWU
"""

def main():
    advisor_list = [
        "philosopher",
        "natural_scientist",
        "artist",
        "treasurer",
        "theologian",
        "master_of_mint",
        "inquisitor",
        "administrator",
        "supervisor",
        "reformer",

        "statesman",
        "naval_reformer",
        "trader",
        "spymaster",
        "colonial_governor",
        "diplomat",
        "navigator",
        "shipwright",
        "ambassador",
        "negotiator",

        "army_reformer",
        "army_organiser",
        "commandant",
        "quartermaster",
        "recruitmaster",
        "fortification_expert",
        "grand_captain",
        "sapper",
        "scout",
        "orator"
    ]

    # GFX - Folder, Split by Gender, Male Count, Female Count
    advisor_configuration = {
        "human_gfx": ["human", True, 26, 11],
        "night_elf_gfx": ["night_elf", True, 21, 7],
        "vrykul_gfx": ["vrykul", True, 17, 1],
        "orc_gfx": ["orc", True, 21, 7],
        "ogre_gfx": ["ogre", False, 21, 21],
        "draenei_gfx": ["draenei", True, 21, 7],
        "troll_gfx": ["troll", True, 21, 7],
        "zandalari_troll_gfx": ["zandalari_troll", True, 7, 7],
        "blood_troll_gfx": ["blood_troll", True, 7, 1],
        "goblin_gfx": ["goblin", True, 9, 7],
        "tauren_gfx": ["tauren", True, 21, 7],
        "high_elf_gfx": ["high_elf", True, 7, 7],
        "qiraji_gfx": ["qiraji", False, 7, 7],
        "demon_gfx": ["demon", False, 21, 21],
        "satyr_gfx": ["satyr", False, 6, 6],
        "naga_gfx": ["naga", True, 4, 7],
        "murloc_gfx": ["murloc", False, 7, 7],
        "scourge_gfx": ["scourge", True, 20, 5],
        "dragon_gfx": ["dragonkin", False, 7, 7],
        "undead_gfx": ["undead", True, 21, 7],
        "gnoll_gfx": ["gnoll", False, 6, 6],
        "centaur_gfx": ["centaur", False, 6, 6],
        "furbolg_gfx": ["furbolg", False, 7, 7],
        "wolvar_gfx": ["wolvar", False, 4, 4],
        "gorloc_gfx": ["gorloc", False, 1, 1],
        "kobold_gfx": ["kobold", False, 1, 1],
        "harpy_gfx": ["harpy", False, 4, 4],
        "quillboar_gfx": ["quillboar", False, 3, 3],
        "titan_gfx": ["titan", False, 1, 1],
        "worgen_gfx": ["worgen", True, 21, 7],
        "arakkoa_gfx": ["arakkoa", False, 7, 7],
        "fallen_arakkoa_gfx": ["fallen_arakkoa", False, 1, 1],
        "tuskarr_gfx": ["tuskarr", False, 1, 1],
        "pandaren_gfx": ["pandaren", True, 21, 7],
        "mantid_gfx": ["mantid", False, 2, 2],
        "mogu_gfx": ["mogu", False, 1, 1],
        "yaungol_gfx": ["yaungol", False, 1, 1],
        "ethereal_gfx": ["ethereal", False, 1, 1],
        "gnome_gfx": ["gnome", True, 15, 7],
        "mecha_gnome_gfx": ["mecha_gnome", True, 7, 7],
        "hozen_gfx": ["hozen", False, 1, 1],
        "saurok_gfx": ["saurok", False, 1, 1],
        "taunka_gfx": ["taunka", False, 1, 1],
        "ice_giant_gfx": ["ice_giant", False, 1, 1],
        "sea_giant_gfx": ["sea_giant", False, 1, 1],
        "mountain_giant_gfx": ["mountain_giant", False, 1, 1],
        "dryad_gfx": ["dryad", False, 1, 1],
        "virmen_gfx": ["virmen", False, 1, 1],
        "void_gfx": ["void", False, 1, 1],
        "zangar_gfx": ["zangar", False, 1, 1],
        "pygmy_gfx": ["pygmy", False, 1, 1],
        "nerubian_gfx": ["nerubian", False, 1, 1],
        "broken_gfx": ["broken", False, 7, 7],
        "dwarf_gfx": ["dwarf", True, 21, 7],
        "fire_elemental_gfx": ["fire_elemental", False, 7, 7],
        "earth_elemental_gfx": ["earth_elemental", False, 3, 3],
        "water_elemental_gfx": ["water_elemental", False, 7, 7],
        "wind_elemental_gfx": ["wind_elemental", False, 7, 7],
        "treant_gfx": ["treant", False, 1, 1],
        "sha_gfx": ["sha", False, 1, 1],
        "demon_hunter_gfx": ["demon_hunter", False, 1, 1],
        "jinyu_gfx": ["jinyu", False, 1, 1],
        "lobster_gfx": ["lobster", False, 1, 1],
        "ghost_gfx": ["ghost", False, 1, 1],
        "magnataur_gfx": ["magnataur", False, 1, 1],
        "trogg_gfx": ["trogg", False, 1, 1],
        "grummle_gfx": ["grummle", False, 1, 1],
        "sethrak_gfx": ["sethrak", False, 4, 4],
        "vulpera_gfx": ["vulpera", True, 7, 7],
        "tortollan_gfx": ["tortollan", False, 3, 3],
        "drogbar_gfx": ["drogbar", False, 7, 7],
        "fungarian_gfx": ["fungarian", False, 4, 4],
        "stone_tolvir_gfx": ["stone_tolvir", False, 4, 4],
        "tolvir_gfx": ["tolvir", False, 4, 4],
        "dark_iron_dwarf_gfx": ["dark_iron_dwarf", True, 7, 7],
        "frost_nymph_gfx": ["frost_nymph", False, 1, 1],
        "crystal_nymph_gfx": ["crystal_nymph", False, 1, 1],
        "blood_elf_gfx": ["blood_elf", True, 21, 7],
        "nightborne_gfx": ["nightborne", True, 4, 3],
        "spriteling_gfx": ["spriteling", False, 1, 1],
        "ooze_gfx": ["ooze", False, 1, 1],
        "illidari_gfx": ["demon_hunter", False, 1, 1],
        "botani_gfx": ["botani", False, 1, 1],
        "saberon_gfx": ["saberon", False, 4, 4],
        "podling_gfx": ["podling", False, 1, 1],
        "rock_flayer_gfx": ["rock_flayer", False, 1, 1],
        "kul_tiran_gfx": ["kul_tiran", True, 7, 7],
        "black_dragon_gfx": ["black_dragon", False, 1, 1],
        "blue_dragon_gfx": ["blue_dragon", False, 1, 1],
        "bronze_dragon_gfx": ["bronze_dragon", False, 1, 1],
        "gray_dragon_gfx": ["infinite_dragon", False, 1, 1],
        "green_dragon_gfx": ["green_dragon", False, 1, 1],
        "nightmare_dragon_gfx": ["nightmare_dragon", False, 1, 1],
        "red_dragon_gfx": ["red_dragon", False, 1, 1],
        "lightforged_draenei_gfx": ["lightforged_draenei", True, 7, 7],
        "void_elf_gfx": ["void_elf", True, 7, 7],
        "gorilla_gfx": ["gorilla", False, 1, 1],
        "iron_dwarf_gfx": ["iron_dwarf", False, 1, 1],
        "dracthyr_gfx": ["dracthyr", False, 7, 7],
        "djaradin_gfx": ["djaradin", False, 1, 1],
        "primalist_gfx": ["primalist", False, 7, 7],
    }

    output = open( "output.txt", "wt")
    output.write("\n")
    output.write("#-----------------")
    output.write("\n")
    output.write("# Auto-generated. Place unique advisors within z_WWU - Advisors - Base.gfx")
    output.write("\n")
    output.write("#-----------------")

    for gfx_type, attributes in advisor_configuration.items():
        folder = attributes[0]
        split_by_gender = attributes[1]
        male_count = attributes[2]
        female_count = attributes[3]

        print(gfx_type)

        output.write("\n")
        output.write("#-----------------")
        output.write("\n")
        output.write("# {0}".format(gfx_type))
        output.write("\n")
        output.write("#-----------------")
        output.write("\n")

        current_advisor_id = 1
        gender_folder = "male"

        # Male
        for type in advisor_list:
            output.write("spriteType = {")
            output.write("\n")
            output.write("\tname = \"GFX_advisor_{gfx_type}_{advisor}\"".format(
                gfx_type=gfx_type,
                advisor=type))
            output.write("\n")
            output.write("\ttexturefile = \"gfx//interface//advisors//{folder}//{gender_folder}//{id}.dds\"".format(
                folder=folder,
                gender_folder=gender_folder,
                id=current_advisor_id
            ))
            output.write("\n")
            output.write("\tnoOfFrames = 1")
            output.write("\n")
            output.write("\tnorefcount = yes")
            output.write("\n")
            output.write("\teffectFile = \"gfx/FX/buttonstate.lua\"")
            output.write("\n")
            output.write("\tloadType = \"INGAME\"")
            output.write("\n")
            output.write("}")
            output.write("\n")

            current_advisor_id = current_advisor_id + 1

            if(current_advisor_id > male_count):
                current_advisor_id = 1

        # Female
        if(split_by_gender):
            gender_folder = "female"

        current_advisor_id = 1

        for type in advisor_list:
            output.write("spriteType = {")
            output.write("\n")
            output.write("\tname = \"GFX_advisor_{gfx_type}_{advisor}_female\"".format(
                gfx_type=gfx_type,
                advisor=type))
            output.write("\n")
            output.write("\ttexturefile = \"gfx//interface//advisors//{folder}//{gender_folder}//{id}.dds\"".format(
                folder=folder,
                gender_folder=gender_folder,
                id=current_advisor_id
            ))
            output.write("\n")
            output.write("\tnoOfFrames = 1")
            output.write("\n")
            output.write("\tnorefcount = yes")
            output.write("\n")
            output.write("\teffectFile = \"gfx/FX/buttonstate.lua\"")
            output.write("\n")
            output.write("\tloadType = \"INGAME\"")
            output.write("\n")
            output.write("}")
            output.write("\n")

            current_advisor_id = current_advisor_id + 1

            if(current_advisor_id > female_count):
                current_advisor_id = 1

    output.close()

if __name__ == "__main__":
    main()