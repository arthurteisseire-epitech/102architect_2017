def print_tab_line(tab):
    line = ""
    for nb in tab:
        if (line != ""):
            line += "\t"
        line += str(nb)
    print(line)

def print_matrix(matrix):
    for tab in matrix:
        print_tab_line(tab)
