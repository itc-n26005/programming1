def perrin(m = 100):
    a, b, c = 3, 0, 2
    results = []
    while a < m:
        results.append(a)
        a, b, c = b, c, a + b
    return results

print(perrin(100))

# p_list = perrin(100000)
p_list = perrin(100)
x_list = list()
for p, n in enumerate(p_list):
    if n == 0:
        continue
    print((n, p), end = ' ')
    if p % n == 0:
        x_list.append(n)

print(x_list)
