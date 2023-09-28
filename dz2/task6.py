a = input()
numbers = [i for i in a if i in map(str, range(10))]
k = int(input())
print(f'{k}-ая цифра в строке {numbers[k - 1]}')
