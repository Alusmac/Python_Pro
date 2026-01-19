import doctest


def transpose_matrix(matrix):
    """
    Transposes a matrix.

    >>> transpose_matrix([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    >>> transpose_matrix([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    >>> transpose_matrix([])
    []
    """
    if not matrix:
        return []
    return list(map(list, zip(*matrix)))


def matrix_multiply(matrix1, matrix2):
    """
    Multiplication of two matrices.

    >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    >>> matrix_multiply([[1, 0], [0, 1]], [[9, 8], [7, 6]])
    [[9, 8], [7, 6]]
    >>> matrix_multiply([], [[1]])
    Traceback (most recent call last):
        ...
    ValueError: Cannot multiply: empty matrix
    """
    if not matrix1 or not matrix2 or not matrix1[0] or not matrix2[0]:
        raise ValueError("Cannot multiply: empty matrix")

    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Cannot multiply: incompatible dimensions")

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


if __name__ == "__main__":
    doctest.testmod()
