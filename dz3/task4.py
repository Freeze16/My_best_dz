def something(a) -> list:
    ans = []
    while a:
        ans.append(a)
        a = input()
    return ans


elements = something(input())
elements_without_repeat = []
print('Элемент | Частота')

for el in elements:
    if el not in elements_without_repeat:
        elements_without_repeat.append(el)
        print(el, '|', elements.count(el))

