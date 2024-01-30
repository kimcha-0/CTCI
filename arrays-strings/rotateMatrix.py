"""Rotate an N x N matrix by 90 degrees can we do this in place?"""


def rotateMatrix(matrix):
    # space: O(n^2)
    # time: O(n^2)
    result = [[0]*len(matrix[0]) for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[-j][i]
    #  (x, y) -> (y, -x)
    return result

print(rotateMatrix([[1, 1, 1], [0, 0, 0], [0, 0, 0]]))
