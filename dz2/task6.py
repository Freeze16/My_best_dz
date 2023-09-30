# a = input()
# numbers = [i for i in a if i in map(str, range(10))]
# k = int(input())
# print(f'{k}-ая цифра в строке {numbers[k - 1]}')

a = input()
k = k0 = int(input())

for i in a:
    if i in map(str, range(10)):
        k -= 1
    if k == 0:
        print(f'{k0}-ая цифра в строке {i}')
