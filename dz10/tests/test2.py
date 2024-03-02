import pytest
from dz10.hash_table import HashTable


@pytest.fixture
def hash_table():
    return HashTable()


@pytest.mark.parametrize(
    ('key', 'expected'),
    [
        ('a', 2),
        ('b', 3),
        ('4', 2),
        ('4a', 4),
    ]
)
def test_hash(key, expected, hash_table):
    assert hash_table.hash_func(key) == expected


def test_set_value(hash_table):
    hash_table.set_value("key1", "value1")
    assert hash_table.get_value("key1") == "value1"
    hash_table.set_value("key2", 3)
    assert hash_table.get_value("key2") == 3


def test_get_value(hash_table):
    hash_table.set_value("key1", "value1")
    assert hash_table.get_value("key1") == "value1"
    assert hash_table.get_value("key2") is None


def test_del_value(hash_table):
    hash_table.set_value("key1", "value1")
    assert hash_table.del_value("key1") is True
    assert hash_table.del_value("key2") is False


def test_load_factor(hash_table):
    hash_table.set_value("key1", "value1")
    hash_table.set_value("key2", 2)
    assert hash_table.load_factor() == 0.4


def test_str(hash_table):
    hash_table.set_value("key1", "value1")
    hash_table.set_value("key2", 3)
    assert str(hash_table) == "{'key1': 'value1', 'key2': 3}"


def test_from_dict(hash_table):
    hash_table.from_dict({'abv': '123', 'gdz': 3, 'a': 1, 'b': 2, 3: 3, 'd': 4})
    assert hash_table.tab == [[['d', 4]], [[3, 3]], [], [['abv', '123']], [], [['gdz', 3]], [], [['a', 1]], [['b', 2]], []]
