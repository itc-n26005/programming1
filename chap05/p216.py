import copy
square = [[1, 4, 9], [16, 25]]
square2 = copy.deepcopy(square)
square[0][0] = 99
square[1] = 999
print(square2)
