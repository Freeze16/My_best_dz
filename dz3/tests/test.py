def enter(a) -> list:
    ans = []
    while a:
        ans.append(a)
        a = input()
    return ans


def test():
    enter('3')
    assert _input('3\n45\n5\n') == ['3', '45', '5']
