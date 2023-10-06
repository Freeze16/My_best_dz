def something(a) -> list:
    ans = []
    while a:
        ans.append(a)
        a = input()
    return ans


print(something(input()))
