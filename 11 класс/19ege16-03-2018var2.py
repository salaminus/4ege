A = [0,7,8,8,1,2,2,3,3,8,5]
n = 10
s = 0
for i in range(2,n+1):
    if A[i-1] < A[i]:
        t = A[i-1]
        A[i-1] = A[i]
        A[i] = t + 1
        s = s + 1
print(s)