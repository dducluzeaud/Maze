

"""Open and read the file containing the maze. Each char in the file will get
   coordinates with a dictionnary
"""
with open("map.txt", "r") as map_file:
    id_line = 0
    coord = {}
    for line in map_file:
        id_column = 0
        for char in line:
            coord[(id_line, id_column)] = char
            id_column += 1
        id_line += 1

    for value in coord.values():
        print(value, end='')
