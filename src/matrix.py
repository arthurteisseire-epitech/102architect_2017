def coord_to_matrix(x, y):
    matrix = [[x], [y], [1]]
    return (matrix)

def matrix_product(A, B):
    row_len = len(A)
    col_len = len(B[0])
    C = [[0 for i in range(col_len)] for i in range(row_len)]
    for row in range(row_len):
        sum_row = 0
        for col in range(col_len):
            C[row][col] = matrix_sum(A, row, B, col)
    return (C)

def matrix_sum(A, row, B, col):
    sum = 0
    for i in range(3):
        sum += A[row][i] * B[i][col]
    return (sum)
