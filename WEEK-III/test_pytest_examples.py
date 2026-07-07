import pytest


@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]


def test_sum(numbers):
    assert sum(numbers) == 15


def test_max(numbers):
    assert max(numbers) == 5


def test_min(numbers):
    assert min(numbers) == 1


def test_append(numbers):
    numbers.append(6)
    assert numbers[-1] == 6


def test_pop(numbers):
    assert numbers.pop() == 5


def test_clear(numbers):
    numbers.clear()
    assert numbers == []


def test_reverse(numbers):
    numbers.reverse()
    assert numbers == [5, 4, 3, 2, 1]


def test_len(numbers):
    assert len(numbers) == 5


def test_contains(numbers):
    assert 3 in numbers


def test_not_contains(numbers):
    assert 10 not in numbers

