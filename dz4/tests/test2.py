from dz4.task2 import fac


def test():
    assert fac(5) == 120
    assert fac(3) == 6
    assert fac(1) == 1
    assert fac(0) == 1
