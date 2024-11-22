import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Реализация Венгерского алгоритма для задачи минимизации.
    
    :param cost_matrix: numpy.ndarray, матрица стоимости (n x n)
    :return: tuple (минимальная стоимость, список соответствий)
    """
    # Шаг 1: Вычитаем минимальное значение из каждой строки
    cost_matrix = cost_matrix.copy()
    for i in range(cost_matrix.shape[0]):
        cost_matrix[i] -= np.min(cost_matrix[i])

    # Шаг 2: Вычитаем минимальное значение из каждого столбца
    for j in range(cost_matrix.shape[1]):
        cost_matrix[:, j] -= np.min(cost_matrix[:, j])

    # Шаг 3: Накладываем минимальное количество линий, чтобы покрыть все нули
    n = cost_matrix.shape[0]
    while True:
        covered_rows = set()
        covered_cols = set()
        marked_zeros = []

        # Помечаем все нули (один ноль на строку и столбец)
        for i in range(n):
            for j in range(n):
                if cost_matrix[i, j] == 0 and i not in covered_rows and j not in covered_cols:
                    marked_zeros.append((i, j))
                    covered_rows.add(i)
                    covered_cols.add(j)

        # Если нулей достаточно, чтобы покрыть матрицу, завершаем
        if len(covered_rows) + len(covered_cols) >= n:
            break

        # Шаг 4: Модифицируем матрицу
        uncovered_rows = set(range(n)) - covered_rows
        uncovered_cols = set(range(n)) - covered_cols

        min_value = np.min([cost_matrix[i, j] for i in uncovered_rows for j in uncovered_cols])

        # Уменьшаем минимальное значение на непокрытых элементах
        for i in uncovered_rows:
            cost_matrix[i] -= min_value
        # Увеличиваем минимальное значение на перекрёстных элементах
        for j in covered_cols:
            cost_matrix[:, j] += min_value

    # Шаг 5: Формируем окончательное соответствие
    row_assignment = [-1] * n
    col_assignment = [-1] * n

    for i, j in marked_zeros:
        row_assignment[i] = j
        col_assignment[j] = i

    # Минимальная стоимость
    total_cost = sum(original_matrix[i, j] for i, j in enumerate(row_assignment))
    return total_cost, row_assignment


# Пример использования
original_matrix = np.array([
    [4, 1, 3, 2],
    [2, 0, 5, 3],
    [3, 2, 2, 3],
    [4, 3, 1, 2]
])

cost, assignment = hungarian_algorithm(original_matrix)
print(f"Минимальная стоимость: {cost}")
print(f"Назначения (строка -> столбец): {assignment}")