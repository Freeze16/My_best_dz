from dz4.task3 import check


def test():
    assert check([34, 'Hello, world!', False])
    assert check('12345')
    assert check(tuple([23, '23']))
    assert not check('1113')
    assert not check(tuple([7, 7]))
