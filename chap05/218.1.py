mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

I = 2
J = 4
mat = [[i * J + j + 1 for j in range(J)] for i in range(I)]
print(mat)
