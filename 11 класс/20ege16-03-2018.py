x = int(input())
a=0; b=0
while x > 0:
    if x%2 > 0:
        a += 1
    else:
        b = b + x%6
    x = x//6
print(a, b)