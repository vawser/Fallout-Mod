import os
import sys
import xylozi_common as com

"""
Generate Artifact releated script for the WWU artifact system
"""

def getScriptPath():
    """ Returns current path of script """
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def build_event(name, event_id):
    os.chdir(getScriptPath())

    template = "template_" + name + ".txt"
    output_name = "output_" + name + ".txt"

    input_list = com.get_csv_list("input.txt", ";")
    template_file = com.get_file_as_string(template)

    outputFile = open(output_name, "wt")

    for entry in input_list:
        new_entry = template_file.format(event_id=event_id, artifact=entry[0], artifact_name=entry[1])
        new_entry = new_entry.replace( "[", "{")
        new_entry = new_entry.replace( "]", "}")
        outputFile.write(new_entry)

        event_id = event_id + 1

    outputFile.close()

def build_custom_localization(name):
    os.chdir(getScriptPath())

    template = "template_custom_localization_" + name + ".txt"
    output_name = "output_custom_localization_" + name + ".txt"

    input_list = com.get_csv_list("input.txt", ";")
    template_file = com.get_file_as_string(template)

    outputFile = open(output_name, "wt")

    for entry in input_list:
        new_entry = template_file.format(artifact=entry[0])
        new_entry = new_entry.replace("[", "{")
        new_entry = new_entry.replace("]", "}")
        outputFile.write(new_entry)

    outputFile.close()

def build_icons():
    os.chdir(getScriptPath())

    template = "template_gfx_icon.txt"
    output_name = "output_gfx_icon.txt"

    input_list = com.get_csv_list("input.txt", ";")
    template_file = com.get_file_as_string(template)

    outputFile = open(output_name, "wt")

    for entry in input_list:
        new_entry = template_file.format(artifact=entry[0])
        new_entry = new_entry.replace("[", "{")
        new_entry = new_entry.replace("]", "}")
        outputFile.write(new_entry)

    outputFile.close()

def build_event_options(name, event_id):
    os.chdir(getScriptPath())

    template = "template_" + name + ".txt"
    output_name = "output_" + name + ".txt"

    input_list = com.get_csv_list("input.txt", ";")
    template_file = com.get_file_as_string(template)

    outputFile = open(output_name, "wt")

    for entry in input_list:
        new_entry = template_file.format(event_id=event_id, artifact=entry[0])
        new_entry = new_entry.replace( "[", "{")
        new_entry = new_entry.replace( "]", "}")
        outputFile.write(new_entry)

        event_id = event_id + 1

    outputFile.close()

def build_triggered_modifiers():
    os.chdir(getScriptPath())

    template = "template_triggered_modifier.txt"
    output_name = "output_triggered_modifier.txt"

    input_list = com.get_csv_list("input.txt", ";")
    template_file = com.get_file_as_string(template)

    outputFile = open(output_name, "wt")

    for entry in input_list:
        new_entry = template_file.format(artifact=entry[0], artifact_name=entry[1])
        new_entry = new_entry.replace("[", "{")
        new_entry = new_entry.replace("]", "}")
        outputFile.write(new_entry)

    outputFile.close()

def build_flags():
    os.chdir(getScriptPath())

    output_name = "output_flags.txt"

    input_list = com.get_csv_list("input.txt", ";")

    outputFile = open(output_name, "wt")

    for entry in input_list:
        new_entry = "has_country_flag = artifact_{artifact}\n".format(artifact=entry[0])
        outputFile.write(new_entry)

    for entry in input_list:
        new_entry = "clr_country_flag = primary_artifact_{artifact}\n".format(artifact=entry[0])
        outputFile.write(new_entry)

    outputFile.close()

def build_reward_list(event_id):
    os.chdir(getScriptPath())

    template = "template_reward_list.txt"
    output_name = "output_reward_list.txt"

    input_list = com.get_csv_list("input.txt", ";")
    template_file = com.get_file_as_string(template)

    outputFile = open(output_name, "wt")

    for entry in input_list:
        new_entry = template_file.format(event_id=event_id, artifact=entry[0])
        new_entry = new_entry.replace("[", "{")
        new_entry = new_entry.replace("]", "}")
        outputFile.write(new_entry)
        event_id = event_id + 1

    outputFile.close()

def build_specific_reward_list(event_id):
    os.chdir(getScriptPath())

    template = "template_specific_reward_list.txt"
    output_name = "output_specific_reward_list.txt"

    input_list = com.get_csv_list("input.txt", ";")
    template_file = com.get_file_as_string(template)

    outputFile = open(output_name, "wt")

    for entry in input_list:
        new_entry = template_file.format(event_id=event_id, artifact=entry[0])
        new_entry = new_entry.replace("[", "{")
        new_entry = new_entry.replace("]", "}")
        outputFile.write(new_entry)
        event_id = event_id + 1

    outputFile.close()

def main():
    event_id = 75

    # GFX
    build_icons()

    # Custom Localization
    build_custom_localization("name")
    build_custom_localization("icon")

    # Event Options
    build_event_options("wwu_artifact_repository_owned", event_id)
    build_event_options("wwu_artifact_repository_unowned", event_id)

    # Events
    build_event("wwu_artifact_repository", event_id)
    build_event("wwu_artifact_heist", event_id)
    build_event("wwu_archaeology", event_id)

    # Triggered Modifiers
    build_triggered_modifiers()

    # Flags
    build_flags()

    # Reward List
    build_reward_list(event_id)
    build_specific_reward_list(event_id)

    input_list = com.get_csv_list("input.txt", ";")

    # Localization - wwu_artifact_repository.1 - owned
    outputFile = open("loc_output_wwu_artifact_repository_owned.txt", "wt")

    for entry in input_list:
        new_entry = " wwu_artifact_repository.1.option.{artifact}: \"{artifact_name}\"\n".format(
            artifact=entry[0], artifact_name=entry[1] )

        outputFile.write(new_entry)

    outputFile.close()

    # Localization - wwu_artifact_repository.1 - unowned
    outputFile = open("loc_output_wwu_artifact_repository_unowned.txt", "wt")

    for entry in input_list:
        new_entry = " wwu_artifact_repository.1.option.unowned.{artifact}: \"§g{artifact_name}§!\"\n".format(
            artifact=entry[0], artifact_name=entry[1])

        outputFile.write(new_entry)

    outputFile.close()

    # Localization - wwu_artifact_repository - Single pages
    outputFile = open("loc_output_wwu_artifact_repository_singles.txt", "wt")

    count = event_id

    for entry in input_list:
        new_entry = " wwu_artifact_repository.{count}.title: \"{artifact_name}\"\n".format(
            count=count, artifact=entry[0], artifact_name=entry[1])

        new_entry = new_entry + " wwu_artifact_repository.{count}.desc: \"\\n[Root.GetArtifactUnlockSpacer]£{artifact}_icon£\\n\\n\\nLORE HERE\\n\\nCurrent Owner:\\n@[current_artifact_owner.GetTag] [current_artifact_owner.GetName]\\n\\nArtifact Effect:\\n§G+10%§! EFFECT\"\n".format(
            count=count, artifact=entry[0], artifact_name=entry[1])

        new_entry = new_entry + " wwu_artifact_repository.{count}.option.make_primary: \"Assign as Primary Artifact\"\n".format(
            count=count)

        new_entry = new_entry + " wwu_artifact_repository.{count}.option.exit: \"Exit\"\n\n".format(
            count=count)

        count = count + 1
        outputFile.write(new_entry)

    outputFile.close()

    # Localization - wwu_artifact_heist - Single pages
    outputFile = open("loc_output_wwu_artifact_heist_singles.txt", "wt")

    count = event_id

    for entry in input_list:
        new_entry = " wwu_artifact_heist.{count}.title: \"Loss of {artifact_name}\"\n".format(
            count=count, artifact=entry[0], artifact_name=entry[1])

        new_entry = new_entry + " wwu_artifact_heist.{count}.desc: \"\\n[Root.GetArtifactUnlockSpacer]£{artifact}_icon£\\n\\n\\nLORE HERE\"\n".format(
            count=count, artifact=entry[0], artifact_name=entry[1])

        new_entry = new_entry + " wwu_artifact_heist.{count}.option.a: \"Curses!\"\n\n".format(
            count=count)

        count = count + 1
        outputFile.write(new_entry)

    outputFile.close()

    # Localization - wwu_archaeology
    outputFile = open("loc_output_wwu_archaeology.txt", "wt")

    count = event_id

    for entry in input_list:
        new_entry = " wwu_archaeology.{count}.title: \"Major Discovery: {artifact_name}\"\n".format(
            count=count, artifact=entry[0], artifact_name=entry[1])

        new_entry = new_entry + " wwu_archaeology.{count}.desc: \"£archaeology_banner£\\n[Root.GetArtifactUnlockSpacer]£{artifact}_icon£\\n\\n\\nLORE HERE\"\n".format(
            count=count, artifact=entry[0], artifact_name=entry[1])

        new_entry = new_entry + " wwu_archaeology.{count}.option.a: \"Excellent find!\"\n\n".format(
            count=count)

        count = count + 1
        outputFile.write(new_entry)

    outputFile.close()

    # Localization - triggered modifiers
    outputFile = open("loc_output_triggered_modifier.txt", "wt")

    for entry in input_list:
        new_entry = " artifact_{artifact}: \"{artifact_name}\"\n".format(
            count=count, artifact=entry[0], artifact_name=entry[1])
        new_entry = new_entry + " desc_artifact_{artifact}: \"\"\n\n".format(
            count=count, artifact=entry[0], artifact_name=entry[1])

        outputFile.write(new_entry)

    outputFile.close()

    # Localization - custom loc - icon strings
    outputFile = open("loc_output_strings.txt", "wt")

    for entry in input_list:
        new_entry = " artifact_icon_{artifact}: \"£{artifact}_icon£\"\n".format(
            artifact=entry[0])

        outputFile.write(new_entry)

    outputFile.write("\n")
    outputFile.close()

    # Localization - custom loc - name strings
    outputFile = open("loc_output_strings.txt", "a")

    for entry in input_list:
        new_entry = " artifact_name_{artifact}: \"{artifact_name}\"\n".format(
            artifact=entry[0], artifact_name=entry[1])

        outputFile.write(new_entry)

    outputFile.write("\n")
    outputFile.close()

    # Localization - UNLOCK_ARTIFACT
    outputFile = open("loc_output_strings.txt", "a")

    for entry in input_list:
        new_entry = " UNLOCK_ARTIFACT_{artifact}: \"You have gained the artifact §Y{artifact_name}§!\"\n".format(
            artifact=entry[0], artifact_name=entry[1])

        outputFile.write(new_entry)

    outputFile.write("\n")
    outputFile.close()

    # Localization - MAKE_PRIMARY_ARTIFACT
    outputFile = open("loc_output_strings.txt", "a")

    for entry in input_list:
        new_entry = " MAKE_PRIMARY_ARTIFACT_{artifact}: \"Make your primary artifact §Y{artifact_name}§!\"\n".format(
            artifact=entry[0], artifact_name=entry[1])

        outputFile.write(new_entry)

    outputFile.write("\n")
    outputFile.close()

    # Localization - IS_PRIMARY_ARTIFACT
    outputFile = open("loc_output_strings.txt", "a")

    for entry in input_list:
        new_entry = " IS_PRIMARY_ARTIFACT_{artifact}: \"§Y{artifact_name}§! is primary artifact.\"\n".format(
            artifact=entry[0], artifact_name=entry[1])

        outputFile.write(new_entry)

    outputFile.write("\n")
    outputFile.close()

    # Localization - NOT_DISCOVERED
    outputFile = open("loc_output_strings.txt", "a")

    for entry in input_list:
        new_entry = " NOT_DISCOVERED_{artifact}: \"§Y{artifact_name}§! has not been discovered yet.\"\n".format(
            artifact=entry[0], artifact_name=entry[1])

        outputFile.write(new_entry)

    outputFile.write("\n")
    outputFile.close()

    # Localization - STEAL_ARTIFACT
    outputFile = open("loc_output_strings.txt", "a")

    for entry in input_list:
        new_entry = " STEAL_ARTIFACT_{artifact}: \"Steal §Y{artifact_name}§! from [artifact_heist_target.GetName].\"\n".format(
            artifact=entry[0], artifact_name=entry[1])

        outputFile.write(new_entry)

    outputFile.write("\n")
    outputFile.close()

    # Debug
    for entry in input_list:
        print("unlock_artifact = {{ artifact = {artifact} }}".format(artifact=entry[0]))

if __name__ == "__main__":
    main()
