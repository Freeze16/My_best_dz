a = input()[1:-1].split(', ')
ans = ''
while a:
    ans += max(a)
    a.remove(max(a))
print(int(ans))
