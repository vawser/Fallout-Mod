import xylozi_common as com

"""
Generate definition.csv file
"""

def main():
    definitions = com.get_csv_list( "definition.csv", ";" )

    colors = []
    new_entries = []
    max_id = 0
    goal_id = 6000

    for entry in definitions:
        id, r,g, b = entry[0], entry[1], entry[2], entry[3]
        colors.append( [ r, g, b ] )
        max_id = id

    for i in range( int(max_id), goal_id ):
        valid = False
        while valid == False:
            color = com.get_random_color()

            if color not in colors:
                valid = True
            else:
                print( "Collision, rerolling.")

        new_entries.append( "{0};{1};{2};{3};x;x".format(i, color[0], color[1], color[2]))

    file = open( "output.txt", "wt")
    for entry in new_entries:
        file.write(entry)
        file.write("\n")
    file.close()

if __name__ == "__main__":
        main()