def F(x):
    return 2 * (x - 1) * (x - 3) + 7
a = -9
b = 9
M = a
R = F(a)
for t in range(a, b + 1):
    if F(t) > R:
        M = t
        R = F(t)
print(M + R)
