import xylozi_common as com
import os

def main():
    groups = {
        "tech_human": "Human",
        "tech_qiraji": "Qiraji",
        "tech_nerubian": "Nerubian",
        "tech_mantid": "Mantid",
        "tech_centaur": "Centaur",
        "tech_draenei": "Draenei",
        "tech_broken": "Broken",
        "tech_red_dragonflight": "Red Dragon",
        "tech_green_dragonflight": "Green Dragon",
        "tech_black_dragonflight": "Black Dragon",
        "tech_blue_dragonflight": "Blue Dragon",
        "tech_bronze_dragonflight": "Bronze Dragon",
        "tech_dwarf": "Dwarf",
        "tech_dark_iron_dwarf": "Dark Dwarf",
        "tech_dryad": "Dryad",
        "tech_frost_nymph": "Frost Nymph",
        "tech_crystal_nymph": "Crystal Nymph",
        "tech_earthen": "Earthen",
        "tech_high_elf": "High Elf",
        "tech_blood_elf": "Blood Elf",
        "tech_nightborne": "Nightborne",
        "tech_night_elf": "Night Elf",
        "tech_furbolg": "Furbolg",
        "tech_gnoll": "Gnoll",
        "tech_gnome": "Gnome",
        "tech_goblin": "Goblin",
        "tech_gorloc": "Gorloc",
        "tech_harpy": "Harpy",
        "tech_hozen": "Hozen",
        "tech_jinyu": "Jinyu",
        "tech_kobold": "Kobold",
        "tech_magnataur": "Magnataur",
        "tech_mogu": "Mogu",
        "tech_murloc": "Murloc",
        "tech_naga": "Naga",
        "tech_ogre": "Ogre",
        "tech_orc": "Orc",
        "tech_pandaren": "Pandaren",
        "tech_pygmy": "Pygmy",
        "tech_quillboar": "Quillboar",
        "tech_satyr": "Satyr",
        "tech_saurok": "Saurok",
        "tech_scourge": "Scourge",
        "tech_spriteling": "Spriteling",
        "tech_tauren": "Tauren",
        "tech_highmountain_tauren": "Highmountain",
        "tech_tolvir": "Tol'vir",
        "tech_titan": "Titanic",
        "tech_trogg": "Trogg",
        "tech_zandalari_troll": "Zandalari",
        "tech_jungle_troll": "Jungle Troll",
        "tech_forest_troll": "Forest Troll",
        "tech_sand_troll": "Sand Troll",
        "tech_frost_troll": "Frost Troll",
        "tech_tuskarr": "Tuskarr",
        "tech_undead": "Undead",
        "tech_vrykul": "Vrykul",
        "tech_wolvar": "Wolvar",
        "tech_yaungol": "Yaungol",
        "tech_nraqi": "N'raqi",
        "tech_void": "Abyssal",
        "tech_demon": "Demonic",
        "tech_ulduar": "Titanic",
        "tech_frost_giant": "Frost Giant",
        "tech_sea_giant": "Sea Giant",
        "tech_frost_dwarf": "Frost Dwarf",
        "tech_grummle": "Grummle",
        "tech_hill_dwarf": "Hill Dwarf",
        "tech_frost_vrykul": "Frost Vrykul",
        "tech_kvaldir": "Kvaldir",
        "tech_blood_troll": "Blood Troll",
        "tech_dark_troll": "Dark Troll",
        "tech_drogbar": "Drogbar",
        "tech_fungarian": "Fungarian",
        "tech_faldorei": "Fal'dorei",
        "tech_nightfallen": "Nightfallen",
        "tech_felblood": "Felblood",
        "tech_felborne": "Felborne",
        "tech_void_elf": "Void Elf",
        "tech_wretched": "Wretched",
        "tech_lost_one": "Lost One",
        "tech_botani": "Botani",
        "tech_podling": "Podling",
        "tech_pale_orc": "Pale Orc",
        "tech_fel_orc": "Fel Orc",
        "tech_arakkoa": "Arakkoa",
        "tech_fallen_arakkoa": "Fallen Arakkoa",
        "tech_ethereal": "Ethereal",
        "tech_sethrak": "Sethrak",
        "tech_sporeling": "Sporeling",
        "tech_saberon": "Saberon",
        "tech_tortollan": "Tortollan",
        "tech_virmen": "Virmen",
        "tech_vulpera": "Vulpera",
        "tech_illidari": "Illidari",
        "tech_elemental_fire": "Fire",
        "tech_elemental_water": "Water",
        "tech_elemental_wind": "Air",
        "tech_elemental_earth": "Earth",
        "tech_worgen": "Worgen",
        "tech_nightmare": "Nightmare",
        "tech_sha": "Sha",
        "tech_rock_flayer": "Rock Flayer",
        "tech_mechagnome": "Mechagnome",
        "tech_iron_dwarf": "Iron Dwarf",
        "tech_dracthyr": "Dracthyr",
        "tech_djaradin": "Djaradin",
        "tech_primalist": "Primalist"

    }

    modifier_groups = {
        "tech_human":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_qiraji":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 1, 0, 1, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_nerubian":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 1, 0, 1, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_mantid":
            [
                [0, 0, 0, 0, 0, 1, 0],  # Inf A
                [0, 0, 0, 0, 1, 0, 0],  # Inf B
                [0, 0, 0, 0, 1, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 1, 0],  # Cav A
                [0, 0, 0, 0, 1, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_centaur":
            [
                [0, 0, -1, -1, 0, 1, 0],  # Inf A
                [0, 0, -1, -1, 1, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 1, 0],  # Cav A
                [0, 0, -1, -1, 1, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_draenei":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_broken":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_red_dragonflight":
            [
                [0, 0, 0, 0, 0, 1, 0],  # Inf A
                [0, 0, 0, 0, 1, 0, 0],  # Inf B
                [0, -1, 0, 0, 1, 1, 0],  # Inf C
                [0, 0, 0, 0, 0, 1, 0],  # Cav A
                [0, 0, 0, 0, 1, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_green_dragonflight":
            [
                [0, 0, 0, 0, 0, 1, 0],  # Inf A
                [0, 0, 0, 0, 1, 0, 0],  # Inf B
                [0, -1, 0, 0, 1, 1, 0],  # Inf C
                [0, 0, 0, 0, 0, 1, 0],  # Cav A
                [0, 0, 0, 0, 1, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_black_dragonflight":
            [
                [0, 0, 0, 0, 0, 1, 0],  # Inf A
                [0, 0, 0, 0, 1, 0, 0],  # Inf B
                [0, -1, 0, 0, 1, 1, 0],  # Inf C
                [0, 0, 0, 0, 0, 1, 0],  # Cav A
                [0, 0, 0, 0, 1, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_blue_dragonflight":
            [
                [0, 0, 0, 0, 0, 1, 0],  # Inf A
                [0, 0, 0, 0, 1, 0, 0],  # Inf B
                [0, -1, 0, 0, 1, 1, 0],  # Inf C
                [0, 0, 0, 0, 0, 1, 0],  # Cav A
                [0, 0, 0, 0, 1, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_bronze_dragonflight":
            [
                [0, 0, 0, 0, 0, 1, 0],  # Inf A
                [0, 0, 0, 0, 1, 0, 0],  # Inf B
                [0, -1, 0, 0, 1, 1, 0],  # Inf C
                [0, 0, 0, 0, 0, 1, 0],  # Cav A
                [0, 0, 0, 0, 1, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_dwarf":
            [
                [0, 0, 0, 1, 0, 0, 0],  # Inf A
                [0, 0, 1, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 2, -1, -1, 0],  # Inf C
                [0, 0, 1, 1, -1, -1, 0],  # Cav A
                [0, 0, 1, 1, -1, -1, 0],  # Cav B
                [0, 0, 1, 0, -1, -1, 0],  # Art A
                [0, 0, 0, 1, -1, -1, 0]   # Art B
            ],
        "tech_dark_iron_dwarf":
            [
                [0, 0, 0, 1, 0, 0, 0],  # Inf A
                [0, 0, 1, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 2, -1, -1, 0],  # Inf C
                [0, 0, 1, 1, -1, -1, 0],  # Cav A
                [0, 0, 1, 1, -1, -1, 0],  # Cav B
                [0, 0, 1, 0, -1, -1, 0],  # Art A
                [0, 0, 0, 1, -1, -1, 0]   # Art B
            ],
        "tech_dryad":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_frost_nymph":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_crystal_nymph":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_earthen":
            [
                [0, 1, 0, 0, 0, 0, 0],  # Inf A
                [0, 1, 0, 0, 0, 0, 0],  # Inf B
                [0, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 1, 0, 0, 0, 0, 0],  # Cav A
                [0, 1, 0, 0, 0, 0, 0],  # Cav B
                [0, 1, 0, 0, 0, 0, 0],  # Art A
                [0, 1, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_high_elf":
            [
                [1, 0, 0, 0, 0, 0, 0],  # Inf A
                [1, 0, 0, 0, 0, 0, 0],  # Inf B
                [1, 0, 0, 0, 0, 0, 0],  # Inf C
                [1, 0, 0, 0, 0, 0, 0],  # Cav A
                [1, 0, 0, 0, 0, 0, 0],  # Cav B
                [1, 0, 0, 0, 0, 0, 0],  # Art A
                [1, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_blood_elf":
            [
                [1, 0, 0, 0, 0, 0, 0],  # Inf A
                [1, 0, 0, 0, 0, 0, 0],  # Inf B
                [1, 0, 0, 0, 0, 0, 0],  # Inf C
                [1, 0, 0, 0, 0, 0, 0],  # Cav A
                [1, 0, 0, 0, 0, 0, 0],  # Cav B
                [1, 0, 0, 0, 0, 0, 0],  # Art A
                [1, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_nightborne":
            [
                [1, 0, 0, 0, 0, 0, 0],  # Inf A
                [1, 0, 0, 0, 0, 0, 0],  # Inf B
                [1, 0, 0, 0, 0, 0, 0],  # Inf C
                [1, 0, 0, 0, 0, 0, 0],  # Cav A
                [1, 0, 0, 0, 0, 0, 0],  # Cav B
                [1, 0, 0, 0, 0, 0, 0],  # Art A
                [1, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_night_elf":
            [
                [1, 0, 0, 0, 0, 0, 0],  # Inf A
                [1, 0, 0, 0, 0, 0, 0],  # Inf B
                [1, 0, 0, 0, 0, 0, 0],  # Inf C
                [1, 0, 0, 0, 0, 0, 0],  # Cav A
                [1, 0, 0, 0, 0, 0, 0],  # Cav B
                [1, 0, 0, 0, 0, 0, 0],  # Art A
                [1, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_furbolg":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_gnoll":
            [
                [0, 0, -1, -1, 1, 0, 0],  # Inf A
                [0, 0, -1, -1, 1, 0, 0],  # Inf B
                [0, 0, -1, -1, 1, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_gnome":
            [
                [0, 0, 1, 1, 0, -1, 0],  # Inf A
                [0, 0, 1, 1, 0, -1, 0],  # Inf B
                [0, 0, 1, 1, 0, -1, 0],  # Inf C
                [0, 0, 1, 1, 0, -1, 0],  # Cav A
                [0, 0, 1, 1, 0, -1, 0],  # Cav B
                [0, 0, 1, 1, 0, -1, 0],  # Art A
                [0, 0, 1, 1, 0, -1, 0]   # Art B
            ],
        "tech_goblin":
            [
                [0, 0, 1, 0, 1, -1, 0],  # Inf A
                [0, 0, 1, 0, 1, -1, 0],  # Inf B
                [0, 0, 1, 0, 1, -1, 0],  # Inf C
                [0, 0, 1, 0, 1, -1, 0],  # Cav A
                [0, 0, 1, 0, 1, -1, 0],  # Cav B
                [0, 0, 1, 0, 1, -1, 0],  # Art A
                [0, 0, 1, 0, 1, -1, 0]   # Art B
            ],
        "tech_gorloc":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_harpy":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_hozen":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_jinyu":
            [
                [0, 1, 0, 0, 0, 0, 0],  # Inf A
                [0, 1, 0, 0, 0, 0, 0],  # Inf B
                [0, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 1, 0, 0, 0, 0, 0],  # Cav A
                [0, 1, 0, 0, 0, 0, 0],  # Cav B
                [0, 1, 0, 0, 0, 0, 0],  # Art A
                [0, 1, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_kobold":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_magnataur":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_mogu":
            [
                [1, 0, 0, 0, 0, 0, 0],  # Inf A
                [1, 0, 0, 0, 0, 0, 0],  # Inf B
                [1, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_murloc":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_naga":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_ogre":
            [
                [0, 0, 0, 0, 1, -1, 0],  # Inf A
                [0, 0, 0, 0, 1, -1, 0],  # Inf B
                [0, 0, 0, 0, 1, -1, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_orc":
            [
                [0, 0, -1, -1, 1, 1, 0],  # Inf A
                [0, 0, -1, -1, 1, 1, 0],  # Inf B
                [0, 0, -1, -1, 1, 1, 0],  # Inf C
                [0, 0, -1, -1, 1, 1, 0],  # Cav A
                [0, 0, -1, -1, 1, 1, 0],  # Cav B
                [0, 0, -1, -1, 1, 1, 0],  # Art A
                [0, 0, -1, -1, 1, 1, 0]   # Art B
            ],
        "tech_pandaren":
            [
                [0, 1, 0, 0, 0, 0, 0],  # Inf A
                [0, 1, 0, 0, 0, 0, 0],  # Inf B
                [0, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 1, 0, 0, 0, 0, 0],  # Cav A
                [0, 1, 0, 0, 0, 0, 0],  # Cav B
                [0, 1, 0, 0, 0, 0, 0],  # Art A
                [0, 1, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_pygmy":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_quillboar":
            [
                [0, 0, -1, -1, 0, 1, 0],  # Inf A
                [0, 0, -1, -1, 0, 1, 0],  # Inf B
                [0, 0, -1, -1, 0, 1, 0],  # Inf C
                [0, 0, -1, -1, 0, 1, 0],  # Cav A
                [0, 0, -1, -1, 0, 1, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_satyr":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_saurok":
            [
                [0, 0, -1, -1, 1, 0, 0],  # Inf A
                [0, 0, -1, -1, 1, 0, 0],  # Inf B
                [0, 0, -1, -1, 1, 0, 0],  # Inf C
                [0, 0, -1, -1, 1, 0, 0],  # Cav A
                [0, 0, -1, -1, 1, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_scourge":
            [
                [2, 2, -1, -1, -1, -1, 0],  # Inf A
                [2, 2, -1, -1, -1, -1, 0],  # Inf B
                [2, 2, -1, -1, -1, -1, 0],  # Inf C
                [2, 2, -1, -1, -1, -1, 0],  # Cav A
                [2, 2, -1, -1, -1, -1, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_spriteling":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_tauren":
            [
                [0, 1, -1, -1, 0, 0, 0],  # Inf A
                [0, 1, -1, -1, 0, 0, 0],  # Inf B
                [0, 1, -1, -1, 0, 0, 0],  # Inf C
                [0, 1, -1, -1, 0, 0, 0],  # Cav A
                [0, 1, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_highmountain_tauren":
            [
                [0, 1, -1, -1, 0, 0, 0],  # Inf A
                [0, 1, -1, -1, 0, 0, 0],  # Inf B
                [0, 1, -1, -1, 0, 0, 0],  # Inf C
                [0, 1, -1, -1, 0, 0, 0],  # Cav A
                [0, 1, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_tolvir":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_titan":
            [
                [1, 1, 0, 0, 0, 0, 0],  # Inf A
                [1, 1, 0, 0, 0, 0, 0],  # Inf B
                [1, 1, 0, 0, 0, 0, 0],  # Inf C
                [1, 1, 0, 0, 0, 0, 0],  # Cav A
                [1, 1, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_trogg":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_zandalari_troll":
            [
                [1, 1, -1, -1, 0, 0, 0],  # Inf A
                [1, 1, -1, -1, 0, 0, 0],  # Inf B
                [1, 1, -1, -1, 0, 0, 0],  # Inf C
                [1, 1, -1, -1, 0, 0, 0],  # Cav A
                [1, 1, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_jungle_troll":
            [
                [1, 1, -1, -1, 0, 0, 0],  # Inf A
                [1, 1, -1, -1, 0, 0, 0],  # Inf B
                [1, 1, -1, -1, 0, 0, 0],  # Inf C
                [1, 1, -1, -1, 0, 0, 0],  # Cav A
                [1, 1, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_forest_troll":
            [
                [1, 1, -1, -1, 0, 0, 0],  # Inf A
                [1, 1, -1, -1, 0, 0, 0],  # Inf B
                [1, 1, -1, -1, 0, 0, 0],  # Inf C
                [1, 1, -1, -1, 0, 0, 0],  # Cav A
                [1, 1, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_sand_troll":
            [
                [1, 1, -1, -1, 0, 0, 0],  # Inf A
                [1, 1, -1, -1, 0, 0, 0],  # Inf B
                [1, 1, -1, -1, 0, 0, 0],  # Inf C
                [1, 1, -1, -1, 0, 0, 0],  # Cav A
                [1, 1, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_frost_troll":
            [
                [1, 1, -1, -1, 0, 0, 0],  # Inf A
                [1, 1, -1, -1, 0, 0, 0],  # Inf B
                [1, 1, -1, -1, 0, 0, 0],  # Inf C
                [1, 1, -1, -1, 0, 0, 0],  # Cav A
                [1, 1, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_tuskarr":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_undead":
            [
                [2, 2, -1, -1, -1, -1, 0],  # Inf A
                [2, 2, -1, -1, -1, -1, 0],  # Inf B
                [2, 2, -1, -1, -1, -1, 0],  # Inf C
                [2, 2, -1, -1, -1, -1, 0],  # Cav A
                [2, 2, -1, -1, -1, -1, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_vrykul":
            [
                [1, 1, 0, 0, 0, 0, 0],  # Inf A
                [1, 1, 0, 0, 0, 0, 0],  # Inf B
                [1, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_wolvar":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_yaungol":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_nraqi":
            [
                [1, 1, 0, 0, 1, 1, 0],  # Inf A
                [1, 1, 0, 0, 1, 1, 0],  # Inf B
                [1, 1, 0, 0, 1, 1, 0],  # Inf C
                [1, 1, 0, 0, 1, 1, 0],  # Cav A
                [1, 1, 0, 0, 1, 1, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_void":
            [
                [1, 1, 0, 0, 1, 1, 0],  # Inf A
                [1, 1, 0, 0, 1, 1, 0],  # Inf B
                [1, 1, 0, 0, 1, 1, 0],  # Inf C
                [1, 1, 0, 0, 1, 1, 0],  # Cav A
                [1, 1, 0, 0, 1, 1, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_demon":
            [
                [1, 1, 0, 0, 1, 1, 0],  # Inf A
                [1, 1, 0, 0, 1, 1, 0],  # Inf B
                [1, 1, 0, 0, 1, 1, 0],  # Inf C
                [1, 1, 0, 0, 1, 1, 0],  # Cav A
                [1, 1, 0, 0, 1, 1, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_ulduar":
            [
                [1, 1, 0, 0, 0, 0, 0],  # Inf A
                [1, 1, 0, 0, 0, 0, 0],  # Inf B
                [1, 1, 0, 0, 0, 0, 0],  # Inf C
                [1, 1, 0, 0, 0, 0, 0],  # Cav A
                [1, 1, 0, 0, 0, 0, 0],  # Cav B
                [1, 1, 0, 0, 0, 0, 0],  # Art A
                [1, 1, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_frost_giant":
            [
                [0, 1, 0, 0, 0, 0, 0],  # Inf A
                [0, 1, 0, 0, 0, 0, 0],  # Inf B
                [0, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_sea_giant":
            [
                [0, 1, 0, 0, 0, 0, 0],  # Inf A
                [0, 1, 0, 0, 0, 0, 0],  # Inf B
                [0, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_frost_dwarf":
            [
                [0, 1, 0, 0, 0, 0, 0],  # Inf A
                [0, 1, 0, 0, 0, 0, 0],  # Inf B
                [0, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_grummle":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_hill_dwarf":
            [
                [0, 0, 0, 1, 0, 0, 0],  # Inf A
                [0, 0, 1, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 2, -1, -1, 0],  # Inf C
                [0, 0, 1, 1, -1, -1, 0],  # Cav A
                [0, 0, 1, 1, -1, -1, 0],  # Cav B
                [0, 0, 1, 0, -1, -1, 0],  # Art A
                [0, 0, 0, 1, -1, -1, 0]   # Art B
            ],
        "tech_frost_vrykul":
            [
                [1, 1, 0, 0, 0, 0, 0],  # Inf A
                [1, 1, 0, 0, 0, 0, 0],  # Inf B
                [1, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_kvaldir":
            [
                [1, 1, 0, 0, 0, 0, 0],  # Inf A
                [1, 1, 0, 0, 0, 0, 0],  # Inf B
                [1, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_blood_troll":
            [
                [1, 1, -1, -1, 0, 0, 0],  # Inf A
                [1, 1, -1, -1, 0, 0, 0],  # Inf B
                [1, 1, -1, -1, 0, 0, 0],  # Inf C
                [1, 1, -1, -1, 0, 0, 0],  # Cav A
                [1, 1, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_dark_troll":
            [
                [1, 1, -1, -1, 0, 0, 0],  # Inf A
                [1, 1, -1, -1, 0, 0, 0],  # Inf B
                [1, 1, -1, -1, 0, 0, 0],  # Inf C
                [1, 1, -1, -1, 0, 0, 0],  # Cav A
                [1, 1, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_drogbar":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_fungarian":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_faldorei":
            [
                [1, 0, 0, 0, 0, 0, 0],  # Inf A
                [1, 0, 0, 0, 0, 0, 0],  # Inf B
                [1, 0, 0, 0, 0, 0, 0],  # Inf C
                [1, 0, 0, 0, 0, 0, 0],  # Cav A
                [1, 0, 0, 0, 0, 0, 0],  # Cav B
                [1, 0, 0, 0, 0, 0, 0],  # Art A
                [1, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_nightfallen":
            [
                [0, 1, 0, 0, 0, 0, 0],  # Inf A
                [0, 1, 0, 0, 0, 0, 0],  # Inf B
                [0, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 1, 0, 0, 0, 0, 0],  # Cav A
                [0, 1, 0, 0, 0, 0, 0],  # Cav B
                [0, 1, 0, 0, 0, 0, 0],  # Art A
                [0, 1, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_felblood":
            [
                [1, 0, 0, 0, 0, 0, 0],  # Inf A
                [1, 0, 0, 0, 0, 0, 0],  # Inf B
                [1, 0, 0, 0, 0, 0, 0],  # Inf C
                [1, 0, 0, 0, 0, 0, 0],  # Cav A
                [1, 0, 0, 0, 0, 0, 0],  # Cav B
                [1, 0, 0, 0, 0, 0, 0],  # Art A
                [1, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_felborne":
            [
                [1, 0, 0, 0, 0, 0, 0],  # Inf A
                [1, 0, 0, 0, 0, 0, 0],  # Inf B
                [1, 0, 0, 0, 0, 0, 0],  # Inf C
                [1, 0, 0, 0, 0, 0, 0],  # Cav A
                [1, 0, 0, 0, 0, 0, 0],  # Cav B
                [1, 0, 0, 0, 0, 0, 0],  # Art A
                [1, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_void_elf":
            [
                [0, 1, 0, 0, 0, 0, 0],  # Inf A
                [0, 1, 0, 0, 0, 0, 0],  # Inf B
                [0, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 1, 0, 0, 0, 0, 0],  # Cav A
                [0, 1, 0, 0, 0, 0, 0],  # Cav B
                [0, 1, 0, 0, 0, 0, 0],  # Art A
                [0, 1, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_wretched":
            [
                [-1, -1, -1, -1, -1, -1, 0],  # Inf A
                [-1, -1, -1, -1, -1, -1, 0],  # Inf B
                [-1, -1, -1, -1, -1, -1, 0],  # Inf C
                [-1, -1, -1, -1, -1, -1, 0],  # Cav A
                [-1, -1, -1, -1, -1, -1, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_lost_one":
            [
                [-1, -1, -1, -1, -1, -1, 0],  # Inf A
                [-1, -1, -1, -1, -1, -1, 0],  # Inf B
                [-1, -1, -1, -1, -1, -1, 0],  # Inf C
                [-1, -1, -1, -1, -1, -1, 0],  # Cav A
                [-1, -1, -1, -1, -1, -1, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_botani":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_podling":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_pale_orc":
            [
                [1, 1, -1, -1, 0, 0, 0],  # Inf A
                [1, 1, -1, -1, 0, 0, 0],  # Inf B
                [1, 1, -1, -1, 0, 0, 0],  # Inf C
                [1, 1, -1, -1, 0, 0, 0],  # Cav A
                [1, 1, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_fel_orc":
            [
                [2, 0, -1, -1, 1, 0, 0],  # Inf A
                [2, 0, -1, -1, 1, 0, 0],  # Inf B
                [2, 0, -1, -1, 1, 0, 0],  # Inf C
                [2, 0, -1, -1, 1, 0, 0],  # Cav A
                [2, 0, -1, -1, 1, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_arakkoa":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_fallen_arakkoa":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_ethereal":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_sethrak":
            [
                [1, 0, 0, 0, 0, 0, 0],  # Inf A
                [1, 0, 0, 0, 0, 0, 0],  # Inf B
                [1, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_sporeling":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_saberon":
            [
                [1, 0, 0, 0, 1, -1, 0],  # Inf A
                [1, 0, 0, 0, 1, -1, 0],  # Inf B
                [1, 0, 0, 0, 1, -1, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_tortollan":
            [
                [-1, 1, 0, 0, 0, 0, 0],  # Inf A
                [-1, 1, 0, 0, 0, 0, 0],  # Inf B
                [-1, 1, 0, 0, 0, 0, 0],  # Inf C
                [-1, 1, 0, 0, 0, 0, 0],  # Cav A
                [-1, 1, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_virmen":
            [
                [0, 0, -1, -1, 0, 0, 0],  # Inf A
                [0, 0, -1, -1, 0, 0, 0],  # Inf B
                [0, 0, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, -1, -1, 0, 0, 0],  # Cav A
                [0, 0, -1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_vulpera":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_illidari":
            [
                [2, -1, 0, 0, 0, 0, 0],  # Inf A
                [2, -1, 0, 0, 0, 0, 0],  # Inf B
                [2, -1, 0, 0, 0, 0, 0],  # Inf C
                [2, -1, 0, 0, 0, 0, 0],  # Cav A
                [2, -1, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_elemental_fire":
            [
                [0, 0, 1, -1, 0, 0, 0],  # Inf A
                [0, 0, 1, -1, 0, 0, 0],  # Inf B
                [0, 0, 1, -1, 0, 0, 0],  # Inf C
                [0, 0, 1, -1, 0, 0, 0],  # Cav A
                [0, 0, 1, -1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_elemental_water":
            [
                [0, 0, -1, 1, 0, 0, 0],  # Inf A
                [0, 0, -1, 1, 0, 0, 0],  # Inf B
                [0, 0, -1, 1, 0, 0, 0],  # Inf C
                [0, 0, -1, 1, 0, 0, 0],  # Cav A
                [0, 0, -1, 1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_elemental_wind":
            [
                [0, 0, 0, 0, 1, -1, 0],  # Inf A
                [0, 0, 0, 0, 1, -1, 0],  # Inf B
                [0, 0, 0, 0, 1, -1, 0],  # Inf C
                [0, 0, 0, 0, 1, -1, 0],  # Cav A
                [0, 0, 0, 0, 1, -1, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_elemental_earth":
            [
                [0, 0, 0, 0, -1, 1, 0],  # Inf A
                [0, 0, 0, 0, -1, 1, 0],  # Inf B
                [0, 0, 0, 0, -1, 1, 0],  # Inf C
                [0, 0, 0, 0, -1, 1, 0],  # Cav A
                [0, 0, 0, 0, -1, 1, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_worgen":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_nightmare":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_sha":
            [
                [1, 1, 0, 0, 0, 0, 0],  # Inf A
                [1, 1, 0, 0, 0, 0, 0],  # Inf B
                [1, 1, 0, 0, 0, 0, 0],  # Inf C
                [1, 1, 0, 0, 0, 0, 0],  # Cav A
                [1, 1, 0, 0, 0, 0, 0],  # Cav B
                [1, 1, 0, 0, 0, 0, 0],  # Art A
                [1, 1, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_rock_flayer":
            [
                [-1, -1, -1, -1, -1, -1, 0],  # Inf A
                [-1, -1, -1, -1, -1, -1, 0],  # Inf B
                [-1, -1, -1, -1, -1, -1, 0],  # Inf C
                [-1, -1, -1, -1, -1, -1, 0],  # Cav A
                [-1, -1, -1, -1, -1, -1, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_mechagnome":
            [
                [0, 0, 1, 1, 0, -1, 0],  # Inf A
                [0, 0, 1, 1, 0, -1, 0],  # Inf B
                [0, 0, 1, 1, 0, -1, 0],  # Inf C
                [0, 0, 1, 1, 0, -1, 0],  # Cav A
                [0, 0, 1, 1, 0, -1, 0],  # Cav B
                [0, 0, 1, 1, 0, -1, 0],  # Art A
                [0, 0, 1, 1, 0, -1, 0]   # Art B
            ],
        "tech_iron_dwarf":
            [
                [0, 1, 0, 0, 0, 0, 0],  # Inf A
                [0, 1, 0, 0, 0, 0, 0],  # Inf B
                [0, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 1, 0, 0, 0, 0, 0],  # Cav A
                [0, 1, 0, 0, 0, 0, 0],  # Cav B
                [0, 1, 0, 0, 0, 0, 0],  # Art A
                [0, 1, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_dracthyr":
            [
                [0, 0, 0, 0, 0, 1, 0],  # Inf A
                [0, 0, 0, 0, 1, 0, 0],  # Inf B
                [0, -1, 0, 0, 1, 1, 0],  # Inf C
                [0, 0, 0, 0, 0, 1, 0],  # Cav A
                [0, 0, 0, 0, 1, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_djaradin":
            [
                [0, 1, 0, 0, 0, 0, 0],  # Inf A
                [0, 1, 0, 0, 0, 0, 0],  # Inf B
                [0, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "tech_primalist":
            [
                [0, 0, 0, 0, 0, 1, 0],  # Inf A
                [0, 0, 0, 0, 1, 0, 0],  # Inf B
                [0, -1, 0, 0, 1, 1, 0],  # Inf C
                [0, 0, 0, 0, 0, 1, 0],  # Cav A
                [0, 0, 0, 0, 1, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ]
    }


    # O. Mor, D. Mor, O. Fire, D. Fire, O. Shock, D. Shock, Manuever

    # Bowman, Archer, Skimisher, Slinger, Spear Thrower
    # Spearman, Axeman, Swordsman, Pikeman, Grunt, Warrior, Berserker, Champion
    # Novice Mage, Mage, Accomplished Mage
    # Scout Cavalry, Skirmish Cavalry, Charge Cavalry
    #
    # Cannon

    units_1 = {
        "inf_a_1":      ["infantry",  1, 2, 1, 1, 1, 1, 1, "Archer", 1, 1, "unit_1"],
        "inf_b_1":      ["infantry",  2, 1, 1, 1, 1, 1, 1, "Warrior", 1, 1, "unit_1"],
        "inf_c_1":      ["infantry", 1, 1, 2, 1, 1, 1, 1, "Spellcaster", 1, 1, "unit_1"],
        "cav_a_1":      ["cavalry",   1, 1, 1, 1, 1, 2, 2, "Light Cavalry", 1, 1, "unit_1"],
        "cav_b_1":      ["cavalry",   1, 1, 1, 1, 2, 1, 2, "Heavy Cavalry", 1, 1, "unit_1"],
        "art_a_1":      ["artillery", 1, 1, 2, 1, 1, 1, 1, "Catapult", 1, 1, "unit_1"],
        "art_b_1":      ["artillery", 1, 1, 1, 2, 1, 1, 1, "Trebuchet", 1, 1, "unit_1"]
    }
    units_2 = {
        "inf_a_2":      ["infantry", 2, 3, 2, 2, 2, 2, 1, "Archer", 1, 2, "unit_2"],
        "inf_b_2":      ["infantry", 3, 2, 2, 2, 2, 2, 1, "Warrior", 1, 2, "unit_2"],
        "inf_c_2":      ["infantry", 2, 2, 3, 2, 2, 2, 1, "Spellcaster", 1, 2, "unit_2"],
        "cav_a_2":      ["cavalry", 2, 2, 2, 2, 2, 3, 2, "Light Cavalry", 1, 2, "unit_2"],
        "cav_b_2":      ["cavalry", 2, 2, 2, 2, 3, 2, 2, "Heavy Cavalry", 1, 2, "unit_2"],
        "art_a_2":      ["artillery", 2, 2, 3, 2, 2, 2, 1, "Catapult", 1, 2, "unit_2"],
        "art_b_2":      ["artillery", 2, 2, 2, 3, 2, 2, 1, "Trebuchet", 1, 2, "unit_2"]
    }
    units_3 = {
        "inf_a_3":      ["infantry", 3, 4, 3, 3, 3, 3, 1, "Archer", 1, 3, "unit_3"],
        "inf_b_3":      ["infantry", 4, 3, 3, 3, 3, 3, 1, "Warrior", 1, 3, "unit_3"],
        "inf_c_3":      ["infantry", 3, 3, 4, 3, 3, 3, 1, "Spellcaster", 1, 3, "unit_3"],
        "cav_a_3":      ["cavalry", 3, 3, 3, 3, 3, 4, 2, "Light Cavalry", 1, 3, "unit_3"],
        "cav_b_3":      ["cavalry", 3, 3, 3, 3, 4, 3, 2, "Heavy Cavalry", 1, 3, "unit_3"],
        "art_a_3":      ["artillery", 3, 3, 4, 3, 3, 3, 1, "Catapult", 1, 3, "unit_3"],
        "art_b_3":      ["artillery", 3, 3, 3, 4, 3, 3, 1, "Trebuchet", 1, 3, "unit_3"]
    }
    units_4 = {
        "inf_a_4":      ["infantry", 4, 5, 4, 4, 4, 4, 1, "Archer", 1, 4, "unit_4"],
        "inf_b_4":      ["infantry", 5, 4, 4, 4, 4, 4, 1, "Warrior", 1, 4, "unit_4"],
        "inf_c_4":      ["infantry", 4, 4, 5, 4, 4, 4, 1, "Spellcaster", 1, 4, "unit_4"],
        "cav_a_4":      ["cavalry", 4, 4, 4, 4, 4, 5, 2, "Light Cavalry", 1, 4, "unit_4"],
        "cav_b_4":      ["cavalry", 4, 4, 4, 4, 5, 4, 2, "Heavy Cavalry", 1, 4, "unit_4"],
        "art_a_4":      ["artillery", 4, 4, 5, 4, 4, 4, 1, "Catapult", 1, 4, "unit_4"],
        "art_b_4":      ["artillery", 4, 4, 4, 5, 4, 4, 1, "Trebuchet", 1, 4, "unit_4"]
    }
    units_5 = {
        "inf_a_5":      ["infantry", 5, 6, 5, 5, 5, 5, 1, "Archer", 1, 5, "unit_5"],
        "inf_b_5":      ["infantry", 6, 5, 5, 5, 5, 5, 1, "Warrior", 1, 5, "unit_5"],
        "inf_c_5":      ["infantry", 5, 5, 6, 5, 5, 5, 1, "Spellcaster", 1, 5, "unit_5"],
        "cav_a_5":      ["cavalry", 5, 5, 5, 5, 5, 6, 2, "Light Cavalry", 1, 5, "unit_5"],
        "cav_b_5":      ["cavalry", 5, 5, 5, 5, 6, 5, 2, "Heavy Cavalry", 1, 5, "unit_5"],
        "art_a_5":      ["artillery", 5, 5, 6, 5, 5, 5, 1, "Catapult", 1, 5, "unit_5"],
        "art_b_5":      ["artillery", 5, 5, 5, 6, 5, 5, 1, "Trebuchet", 1, 5, "unit_5"]
    }

    unit_lists = [ units_1, units_2, units_3, units_4, units_5 ]

    tech = open( "tech.txt", "wt")
    loc = open( "loc.txt", "wt")

    os.chdir( os.getcwd() + "//output//")

    block_1 = ""
    block_2 = ""
    block_3 = ""
    block_4 = ""
    block_5 = ""

    # Tech Group
    for group, title in groups.items():
        pretty_group = group.replace( "tech_", "")

        # Unit List
        for unit_list in unit_lists:

            print(pretty_group)
            idx = 0

            # Unit Entry
            for name, stats in unit_list.items():
                print(name)

                unit_type = stats[0]

                off_morale = stats[1]
                def_morale = stats[2]
                off_fire = stats[3]
                def_fire = stats[4]
                off_shock = stats[5]
                def_shock = stats[6]
                manuever = stats[7]

                localized_name = stats[8]
                manpower = stats[9]
                enable_type = stats[10]
                icon_string = stats[11]

                # Apply modifiers
                current_modifiers = modifier_groups[group][idx]
                idx = idx + 1

                off_morale = off_morale + current_modifiers[0]
                def_morale = def_morale + current_modifiers[1]
                off_fire = off_fire + current_modifiers[2]
                def_fire = def_fire + current_modifiers[3]
                off_shock = off_shock + current_modifiers[4]
                def_shock = def_shock + current_modifiers[5]
                manuever = manuever + current_modifiers[6]

                if off_morale < 0: off_morale = 0
                if def_morale < 0: def_morale = 0
                if off_fire < 0: off_fire = 0
                if def_fire < 0: def_fire = 0
                if off_shock < 0: off_shock = 0
                if def_shock < 0: def_shock = 0
                if manuever < 0: manuever = 0

                # Write unit file
                file = open( "{0}_{1}.txt".format(pretty_group, name), "wt")

                file.write( "type = {0}\n".format(unit_type))
                file.write("unit_type = {0}\n".format(group))
                file.write("\n")
                file.write("maneuver = {0}\n".format(manuever))
                file.write("offensive_morale = {0}\n".format(off_morale))
                file.write("defensive_morale = {0}\n".format(def_morale))
                file.write("offensive_fire = {0}\n".format(off_fire))
                file.write("defensive_fire = {0}\n".format(def_fire))
                file.write("offensive_shock = {0}\n".format(off_shock))
                file.write("defensive_shock = {0}\n".format(def_shock))

                if manpower > 1:
                    file.write("\nmanpower = {0}\n".format(manpower))

                file.write("\n")
                file.close()

                if enable_type == 1:
                    block_1 = block_1 + "enable = {0}_{1}\n".format(group,name)
                if enable_type == 2:
                    block_2 = block_2 + "enable = {0}_{1}\n".format(group,name)
                if enable_type == 3:
                    block_3 = block_3 + "enable = {0}_{1}\n".format(group,name)
                if enable_type == 4:
                    block_4 = block_4 + "enable = {0}_{1}\n".format(group,name)
                if enable_type == 5:
                    block_5 = block_5 + "enable = {0}_{1}\n".format(group,name)

                group_name = group.replace( "tech_", "" )

                loc.write(" {0}_{1}: \"£{4}£ {2} {3}\"\n".format(group_name, name, title, localized_name, icon_string))
                loc.write(" {0}_{1}DESCR: \"\"\n".format(group_name, name))



        loc.write("\n")

    tech.write(block_1)
    tech.write("\n")
    tech.write(block_2)
    tech.write("\n")
    tech.write(block_3)
    tech.write("\n")
    tech.write(block_4)
    tech.write("\n")
    tech.write(block_5)
    tech.write("\n")

    tech.close()
    loc.close()

if __name__ == "__main__":
    main()