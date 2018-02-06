k = 0
a = []
n = 5
for i in range (0, n):
    a.append(int(input()))
    if (a[i] % 3 == 0 and a[i] % 10 == 7):
        a[i] = -1
        k += 1
for i in range(0, n):
    if a[i] == -1:
        a[i] = k
    print(a[i])
