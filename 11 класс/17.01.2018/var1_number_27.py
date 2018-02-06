k = 0
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for j in range(0,n-2):
    for i in range(1,n):
        if ((a[j] + a[i]) % 8 == 0):
            k +=1
print(k)
