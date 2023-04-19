import xylozi_common as com
import os

def main():
    groups = {
        "westerosi": "Westerosi",
        "essosian": "Essosian",
        "ghiscari": "Ghiscari",
        "quartheen": "Qartheen",
        "naathi": "Naathi",
        "farosi": "Farosi",
        "yiti": "Yitish",
        "hyrkooni": "Hyrkooni",
        "nefer": "Neferi",
        "stepstones": "Stepstone",
        "ibbenese": "Ibbenese",
        "summer_islanders": "Summer Islander",
        "valyrian": "Valyrian",
        "asshai": "Asshai",
        "white_walker": "White Walker",
        "bloodless": "Bloodless",
        "dothraki": "Dothraki",
        "jogos_nhai": "Jogos Nhai",
        "wildling": "Wildling",
        "mossovi": "Mossovi",
        "sothoryosi": "Sothoryosi",
        "ulthosi": "Ulthosi",
        "fishfolk": "Fishfolk",
        "shadowfolk": "Shadowfolk",
        "stonemen": "Stonemen",
        "cannibal": "Cannibal",
        "kdathi": "K'Dathi",
    }

    # O. Mor, D. Mor, O. Fire, D. Fire, O. Shock, D. Shock, Manuever

    modifier_groups = {
        "westerosi":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "essosian":
            [
                [0, 0, 0, 0, 0, 0, 0],  # Inf A
                [0, 0, 0, 0, 0, 0, 0],  # Inf B
                [0, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "ghiscari":
            [
                [1, -1, 0, 0, 1, 0, 0],  # Inf A
                [1, -1, 0, 0, 1, 0, 0],  # Inf B
                [1, -1, 0, 0, 1, 0, 0],  # Inf C
                [1, -1, 0, 0, 0, 0, 0],  # Cav A
                [1, -1, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "quartheen":
            [
                [-1, 0, 1, 1, 0, 0, 0],  # Inf A
                [-1, 0, 1, 1, 0, 0, 0],  # Inf B
                [-1, 0, 1, 1, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "naathi":
            [
                [-1, 1, 0, 0, 0, 2, 0],  # Inf A
                [-1, 1, 0, 0, 0, 2, 0],  # Inf B
                [-1, 1, 0, 0, 0, 2, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "farosi":
            [
                [0, 0, 0, 0, 1, 0, 0],  # Inf A
                [0, 0, 0, 0, 1, 0, 0],  # Inf B
                [0, 0, 0, 0, 1, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "yiti":
            [
                [1, 1, 0, 0, 0, 0, 0],  # Inf A
                [1, 1, 0, 0, 0, 0, 0],  # Inf B
                [1, 1, 0, 0, 0, 0, 0],  # Inf C
                [1, 1, 0, 0, 0, 0, 0],  # Cav A
                [1, 1, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "hyrkooni":
            [
                [0, 1, 0, 1, 0, 0, 0],  # Inf A
                [0, 1, 0, 1, 0, 0, 0],  # Inf B
                [0, 1, 0, 1, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "nefer":
            [
                [0, 0, 1, 0, 0, 0, 0],  # Inf A
                [0, 0, 1, 0, 0, 0, 0],  # Inf B
                [0, 0, 1, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "stepstones":
            [
                [0, 0, 0, 0, 1, 0, 0],  # Inf A
                [0, 0, 0, 0, 1, 0, 0],  # Inf B
                [0, 0, 0, 0, 1, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "ibbenese":
            [
                [0, 2, -1, -1, 0, 0, 0],  # Inf A
                [0, 2, -1, -1, 0, 0, 0],  # Inf B
                [0, 2, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "summer_islanders":
            [
                [0, 1, 0, 0, 0, 0, 0],  # Inf A
                [0, 1, 0, 0, 0, 0, 0],  # Inf B
                [0, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "valyrian":
            [
                [1, 1, 0, 0, 0, 0, 0],  # Inf A
                [1, 1, 0, 0, 0, 0, 0],  # Inf B
                [1, 1, 0, 0, 0, 0, 0],  # Inf C
                [1, 1, 0, 0, 0, 0, 0],  # Cav A
                [1, 1, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "asshai":
            [
                [0, -1, 2, 1, 0, 0, 0],  # Inf A
                [0, -1, 2, 1, 0, 0, 0],  # Inf B
                [0, -1, 2, 1, 0, 0, 0],  # Inf C
                [0, -1, 2, 1, 0, 0, 0],  # Cav A
                [0, -1, 2, 1, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "white_walker":
            [
                [2, 2, 2, 2, 2, 2, 0],  # Inf A
                [2, 2, 2, 2, 2, 2, 0],  # Inf B
                [2, 2, 2, 2, 2, 2, 0],  # Inf C
                [2, 2, 2, 2, 2, 2, 0],  # Cav A
                [2, 2, 2, 2, 2, 2, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "bloodless":
            [
                [1, 0, 0, 0, 0, 0, 0],  # Inf A
                [1, 0, 0, 0, 0, 0, 0],  # Inf B
                [1, 0, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "dothraki":
            [
                [1, 0, 0, 0, 0, 0, 0],  # Inf A
                [1, 0, 0, 0, 0, 0, 0],  # Inf B
                [1, 0, 0, 0, 0, 0, 0],  # Inf C
                [2, 1, 0, 0, 1, 1, 0],  # Cav A
                [2, 1, 0, 0, 1, 1, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "jogos_nhai":
            [
                [1, 0, 0, 0, 0, 0, 0],  # Inf A
                [1, 0, 0, 0, 0, 0, 0],  # Inf B
                [1, 0, 0, 0, 0, 0, 0],  # Inf C
                [2, 1, 0, 0, 1, 1, 0],  # Cav A
                [2, 1, 0, 0, 1, 1, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "wildling":
            [
                [1, 1, -1, -1, 0, 0, 0],  # Inf A
                [1, 1, -1, -1, 0, 0, 0],  # Inf B
                [1, 1, -1, -1, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "mossovi":
            [
                [0, 1, 0, 0, 0, 0, 0],  # Inf A
                [0, 1, 0, 0, 0, 0, 0],  # Inf B
                [0, 1, 0, 0, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "sothoryosi":
            [
                [0, 0, 0, 0, 1, 0, 0],  # Inf A
                [0, 0, 0, 0, 1, 0, 0],  # Inf B
                [0, 0, 0, 0, 1, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "ulthosi":
            [
                [0, 0, 0, 0, 0, 1, 0],  # Inf A
                [0, 0, 0, 0, 0, 1, 0],  # Inf B
                [0, 0, 0, 0, 0, 1, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "fishfolk":
            [
                [-1, -1, 0, 0, 0, 0, 0],  # Inf A
                [-1, -1, 0, 0, 0, 0, 0],  # Inf B
                [-1, -1, 0, 0, 0, 0, 0],  # Inf C
                [-1, -1, 0, 0, 0, 0, 0],  # Cav A
                [-1, -1, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "shadowfolk":
            [
                [0, 0, 1, 1, 0, 0, 0],  # Inf A
                [0, 0, 1, 1, 0, 0, 0],  # Inf B
                [0, 0, 1, 1, 0, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "stonemen":
            [
                [-1, 1, 0, 0, 0, 0, 0],  # Inf A
                [-1, 1, 0, 0, 0, 0, 0],  # Inf B
                [-1, 1, 0, 0, 0, 0, 0],  # Inf C
                [-1, 1, 0, 0, 0, 0, 0],  # Cav A
                [-1, 1, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "cannibal":
            [
                [0, 0, -1, -1, 2, 0, 0],  # Inf A
                [0, 0, -1, -1, 2, 0, 0],  # Inf B
                [0, 0, -1, -1, 2, 0, 0],  # Inf C
                [0, 0, 0, 0, 0, 0, 0],  # Cav A
                [0, 0, 0, 0, 0, 0, 0],  # Cav B
                [0, 0, 0, 0, 0, 0, 0],  # Art A
                [0, 0, 0, 0, 0, 0, 0]   # Art B
            ],
        "kdathi":
            [
                [1, 1, 1, 1, 0, 0, 0],  # Inf A
                [1, 1, 1, 1, 0, 0, 0],  # Inf B
                [1, 1, 1, 1, 0, 0, 0],  # Inf C
                [1, 1, 1, 1, 0, 0, 0],  # Cav A
                [1, 1, 1, 1, 0, 0, 0],  # Cav B
                [1, 1, 1, 1, 0, 0, 0],  # Art A
                [1, 1, 1, 1, 0, 0, 0]   # Art B
            ],
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
        "inf_c_1":      ["infantry", 1, 1, 2, 1, 1, 1, 1, "Crossbowman", 1, 1, "unit_1"],
        "cav_a_1":      ["cavalry",   1, 1, 1, 1, 1, 2, 2, "Light Cavalry", 1, 1, "unit_1"],
        "cav_b_1":      ["cavalry",   1, 1, 1, 1, 2, 1, 2, "Heavy Cavalry", 1, 1, "unit_1"],
        "art_a_1":      ["artillery", 1, 1, 2, 1, 1, 1, 1, "Catapult", 1, 1, "unit_1"],
        "art_b_1":      ["artillery", 1, 1, 1, 2, 1, 1, 1, "Trebuchet", 1, 1, "unit_1"]
    }
    units_2 = {
        "inf_a_2":      ["infantry", 2, 3, 2, 2, 2, 2, 1, "Archer", 1, 2, "unit_2"],
        "inf_b_2":      ["infantry", 3, 2, 2, 2, 2, 2, 1, "Warrior", 1, 2, "unit_2"],
        "inf_c_2":      ["infantry", 2, 2, 3, 2, 2, 2, 1, "Crossbowman", 1, 2, "unit_2"],
        "cav_a_2":      ["cavalry", 2, 2, 2, 2, 2, 3, 2, "Light Cavalry", 1, 2, "unit_2"],
        "cav_b_2":      ["cavalry", 2, 2, 2, 2, 3, 2, 2, "Heavy Cavalry", 1, 2, "unit_2"],
        "art_a_2":      ["artillery", 2, 2, 3, 2, 2, 2, 1, "Catapult", 1, 2, "unit_2"],
        "art_b_2":      ["artillery", 2, 2, 2, 3, 2, 2, 1, "Trebuchet", 1, 2, "unit_2"]
    }
    units_3 = {
        "inf_a_3":      ["infantry", 3, 4, 3, 3, 3, 3, 1, "Archer", 1, 3, "unit_3"],
        "inf_b_3":      ["infantry", 4, 3, 3, 3, 3, 3, 1, "Warrior", 1, 3, "unit_3"],
        "inf_c_3":      ["infantry", 3, 3, 4, 3, 3, 3, 1, "Crossbowman", 1, 3, "unit_3"],
        "cav_a_3":      ["cavalry", 3, 3, 3, 3, 3, 4, 2, "Light Cavalry", 1, 3, "unit_3"],
        "cav_b_3":      ["cavalry", 3, 3, 3, 3, 4, 3, 2, "Heavy Cavalry", 1, 3, "unit_3"],
        "art_a_3":      ["artillery", 3, 3, 4, 3, 3, 3, 1, "Catapult", 1, 3, "unit_3"],
        "art_b_3":      ["artillery", 3, 3, 3, 4, 3, 3, 1, "Trebuchet", 1, 3, "unit_3"]
    }
    units_4 = {
        "inf_a_4":      ["infantry", 4, 5, 4, 4, 4, 4, 1, "Archer", 1, 4, "unit_4"],
        "inf_b_4":      ["infantry", 5, 4, 4, 4, 4, 4, 1, "Warrior", 1, 4, "unit_4"],
        "inf_c_4":      ["infantry", 4, 4, 5, 4, 4, 4, 1, "Crossbowman", 1, 4, "unit_4"],
        "cav_a_4":      ["cavalry", 4, 4, 4, 4, 4, 5, 2, "Light Cavalry", 1, 4, "unit_4"],
        "cav_b_4":      ["cavalry", 4, 4, 4, 4, 5, 4, 2, "Heavy Cavalry", 1, 4, "unit_4"],
        "art_a_4":      ["artillery", 4, 4, 5, 4, 4, 4, 1, "Catapult", 1, 4, "unit_4"],
        "art_b_4":      ["artillery", 4, 4, 4, 5, 4, 4, 1, "Trebuchet", 1, 4, "unit_4"]
    }
    units_5 = {
        "inf_a_5":      ["infantry", 5, 6, 5, 5, 5, 5, 1, "Archer", 1, 5, "unit_5"],
        "inf_b_5":      ["infantry", 6, 5, 5, 5, 5, 5, 1, "Warrior", 1, 5, "unit_5"],
        "inf_c_5":      ["infantry", 5, 5, 6, 5, 5, 5, 1, "Crossbowman", 1, 5, "unit_5"],
        "cav_a_5":      ["cavalry", 5, 5, 5, 5, 5, 6, 2, "Light Cavalry", 1, 5, "unit_5"],
        "cav_b_5":      ["cavalry", 5, 5, 5, 5, 6, 5, 2, "Heavy Cavalry", 1, 5, "unit_5"],
        "art_a_5":      ["artillery", 5, 5, 6, 5, 5, 5, 1, "Catapult", 1, 5, "unit_5"],
        "art_b_5":      ["artillery", 5, 5, 5, 6, 5, 5, 1, "Trebuchet", 1, 5, "unit_5"]
    }

    unit_lists = [ units_1, units_2, units_3, units_4, units_5 ]

    tech = open( "tech.txt", "wt")
    loc = open( "loc.txt", "wt")

    os.chdir( os.getcwd() + "//asoiaf_output//")

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