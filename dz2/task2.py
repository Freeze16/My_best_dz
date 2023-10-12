from itertools import permutations

a, b = input(), []
while a:
    b.append(a)
    a = input()

x = permutations(b)  # придумал, что смог
nx = [int(''.join(i)) for i in x]
print(max(nx))
