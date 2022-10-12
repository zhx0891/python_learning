a = [(7, 1, 6), (2, 4, 5), (2, 0, 8), (3, 3), (1, 2, 4, 6)]
print(max(a))
print(min(a))
print(min(a, key=lambda x: len(x)))
print(max(a, key=len(a)))
print(max(a, key=lambda x: x[1]))
