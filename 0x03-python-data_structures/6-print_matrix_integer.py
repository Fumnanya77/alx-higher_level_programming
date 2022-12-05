def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:2d}".format(col), end=""),
        print()
