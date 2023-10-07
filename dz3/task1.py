def enter(a) -> list:
    ans = []
    while a:
        ans.append(a)
        a = input()
    return ans


if __name__ == '__main__':
    print(enter(input()))
