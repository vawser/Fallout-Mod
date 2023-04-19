import xylozi_common as com
import os

"""
Generate group-based triggered modifier script and localization
"""

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

    template = com.get_file_as_string("template.txt")

    os.chdir(os.getcwd() + "//output//")

    file = open("triggered_modifiers.txt", "wt")
    loc_file = open("loc_triggered_modifiers.txt", "wt")

    for group, title in groups.items():
        trigger = group
        group = group.replace("tech_", "")
        entry = template.format(group=group, trigger=trigger, title=title)
        entry = entry.replace("[", "{")
        entry = entry.replace("]", "}")

        file.write(entry)

        loc_file.write( " {group}_administration: \"{title} Administration\"\n"
                        .format(group=group, title=title))
        loc_file.write( " desc_{group}_administration: \"\"\n"
                        .format(group=group, title=title))
        loc_file.write( " {group}_military: \"{title} Military\"\n"
                        .format(group=group, title=title))
        loc_file.write( " desc_{group}_military: \"\"\n\n"
                        .format(group=group, title=title))

    file.close()
    loc_file.close()

if __name__ == "__main__":
    main()