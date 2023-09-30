a = input()
k = k0 = int(input())

for i in a:
    if i.isdigit():
        k -= 1
    if k == 0:
        print(f'{k0}-ая цифра в строке {i}')
