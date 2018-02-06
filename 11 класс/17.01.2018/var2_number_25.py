k = 0
a = []
n = 5
for i in range (0, n):
    a.append(int(input()))
    if (a[i] % 7 == 0 and a[i] % 10 == 3):
        k += 1

print(k)
