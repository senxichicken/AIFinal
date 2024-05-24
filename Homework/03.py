'''複製，使用ChatGPT完成'''

import numpy as np


def pivot(mat, row, col):
    irows, icols = mat.shape
    new_mat = np.zeros_like(mat)

    new_mat[row, :] = mat[row, :] / mat[row, col]
    for i in range(irows):
        if i != row:
            new_mat[i, :] = mat[i, :] - mat[row, :] * mat[i, col] / mat[row, col]
    return new_mat

def simplex(c, A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    c = np.array(c, dtype=float)

    irows, icols = A.shape
    mat = np.zeros((irows + 1, icols + 1))
    mat[:-1, :-1] = A
    mat[:-1, -1] = b
    mat[-1, :-1] = -c

    while np.any(mat[-1, :-1] < 0):
        col = np.argmin(mat[-1, :-1])
        if np.all(mat[:-1, col] <= 0):
            raise ValueError("Linear program is unbounded.")
        row_ratios = mat[:-1, -1] / mat[:-1, col]
        row_ratios[mat[:-1, col] <= 0] = np.inf
        row = np.argmin(row_ratios)
        mat = pivot(mat, row, col)

    solution = np.zeros(icols)
    for i in range(icols):
        if np.any(mat[:, i] == 1) and np.all(np.count_nonzero(mat[:, i]) == 1):
            solution[i] = mat[np.where(mat[:, i] == 1)[0][0], -1]

    return solution, mat[-1, -1]

# 目標係數
c = [3, 2, 5]

# 限制條件的係數矩陣 A 和常數項 b
A = [
    [1, 1, 0],
    [2, 0, 1],
    [0, 1, 2]
]
b = [10, 9, 11]

solution, optimal_value = simplex(c, A, b)

print("Optimal solution (x, y, z):", solution)
print("Optimal value:", optimal_value)

'''
輸出
Optimal solution (x, y, z): [3.4 6.6 2.2]
Optimal value: 34.4
'''