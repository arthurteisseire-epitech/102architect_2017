def print_tab_line(tab):
    line = ""
    for nb in tab:
        if (line != ""):
            line += "\t"
        if (nb > -0.01 and nb < 0):
            nb *= -1
        line += str(format(round(nb, 2), '.2f'))
    print(line)

def print_matrix(matrix):
    for tab in matrix:
        print_tab_line(tab)
