def func_square(*args):
    results = []
    for n in args:
        results.append(n * n)
    return results

#number = [1, 2, 3, 4]
#print(func_square(*number))
many_numbers = list(range(100))
print(func_square(*many_numbers))
