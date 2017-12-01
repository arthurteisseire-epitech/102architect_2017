def print_res(x, y, xpos):
    if (xpos[0][0] > -0.01 and xpos[0][0] < 0):
        xpos[0][0] *= -1
    if (xpos[1][0] > -0.01 and xpos[1][0] < 0):
        xpos[1][0] *= -1
    print("(%d,%d) => (%.2f,%.2f)" %(x, y, xpos[0][0], xpos[1][0]))
