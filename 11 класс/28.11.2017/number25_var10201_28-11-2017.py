a = [1, 7, 77, 123]
n = 4
l = 1
m = 1
b = 0
k = 0
for i in range(0,n):
    #a.append(int(input()))
    b = a[i]
    l = 1
    m = 1
    while b > 9:
        b = b // 10
        l += 1
    b = a[i]
    while b > 7:
        b = b // 8
        m += 1
    if l == m:
        k += 1
print(k)
