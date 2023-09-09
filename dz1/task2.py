a = int(input())
b = int(input())
c = int(input())
d = int(input())
f = int(input())

try:
    ans = (a * b - c) / (f - d)
    print(ans)
except ZeroDivisionError:
    print('Делить на ноль нельзя!')