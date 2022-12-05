def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print(f"{:2d}".format(col), end=""),
        print()
