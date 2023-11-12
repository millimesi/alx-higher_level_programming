#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    ite = 0
    for li in matrix:
        for i in range(len(li)):
            if i == (len(li) - 1):
                print("{:d}".format(matrix[ite][i]), end="")
            else:
                print("{:d}".format(matrix[ite][i]), end=" ")
        ite += 1
        print()