x = int(input())
y = int(input())

summa = 0
for i in range(x, y + 1):
    if i % 5 == 0:
        summa += i
print(summa)
