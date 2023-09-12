a = float(input())
b = float(input())
c = float(input())
d = float(input())
f = float(input())

try:
    print((a * b - c) / (f - d))
except ZeroDivisionError:
    print('Делить на ноль нельзя!')

# if f == d:
#     print('Делить на ноль нельзя!')
# else:
#     print((a * b - c) / (f - d))
