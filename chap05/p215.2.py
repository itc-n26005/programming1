import copy
square = [[1, 4, 9], [16, 25]]
square2 = copy.copy(square)
square[0] = [36]
print(square)
print(square2)
