import numpy as np


def gauss(A, B, rd):
    column = 0

    if np.linalg.det(A) == 0:
        return -1

    while column < len(B):
        current_row = None
        # Ищем максимальный по модулю элемент в N столбце
        for r in range(column, len(A)):
            if (current_row is None) or \
                    (abs(A[r][column]) > abs(A[current_row][column])):
                current_row = r
        # решений нет
        if current_row is None:
            return -1

        if current_row != column:
            # Переставляем строку с найденным элементом повыше
            A[current_row], A[column] = A[column], A[current_row]
            B[current_row], B[column] = B[column], B[current_row]

        # Нормализуем строку с найденным элементом
        B[column] /= A[column][column]
        A[column] = [a / A[column][column] for a in A[column]]

        # Обрабатываем нижележащие строки
        for r in range(column + 1, len(A)):
            B[r] += B[column] * -A[r][column]
            A[r] = [(a + k * -A[r][column]) for a, k in zip(A[r], A[column])]
        column += 1

    res = [0 for a in range(len(A))]

    # Матрица приведена к треугольному виду, считаем решение
    for i in range(len(B)-1, -1, -1):
        res[i] = round(B[i] - sum(x * a for x, a in zip(
            res[(i + 1):],
            A[i][(i + 1):]
            )), rd)

    return res
