d = []
s = 0
#заполнение списка нулевыми значениями
#for i in range(8):
#    d.append(0)
# через генератор списка
#d = [0 for i in range(8)]
d = [0] * 8
print(d)

n = int(input())
for i in range(n):
    x = int(input())
    d[x % 8] += 1
print(d)

s = (d[0] * (d[0] - 1) + d[4] * (d[4] - 1)) // 2
for i in range(1, 4):
    s += d[i] * d[8-i] 

print(s)

