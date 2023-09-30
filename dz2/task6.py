a = input()
k = k0 = int(input())

for i in a:
    if i.isdigit():
        k -= 1
        if not k:
            print(f'{k0}-ая цифра в строке {i}')

