import pytest
from dz10.hash_table import HashTable

table_1 = HashTable()


@pytest.mark.parametrize(
    ('key', 'expected'),
    [
        ('a', 2),
        ('b', 3),
        ('4', 2),
        ('4a', 4),
    ]
)
def test_hash(key, expected):
    assert table_1.hash_func(key) == expected


@pytest.fixture
def hash_table():
    return HashTable(10)


def test_set_value(hash_table):
    hash_table.set_value("key1", "value1")
    assert hash_table.get_value("key1") == "value1"


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
    hash_table.set_value("key2", "value2")
    assert hash_table.load_factor() == 0.2


def test_str(hash_table):
    hash_table.set_value("key1", "value1")
    hash_table.set_value("key2", "value2")
    assert hash_table.__str__() == '{"key2": "value2", "key1": "value1"}'
