from math import ceil, floor

x = ceil(float(input()))
y = floor(float(input()))

summa = 0
for i in range(x, y + 1):
    if i % 5 == 0:
        summa += i
print(summa)
