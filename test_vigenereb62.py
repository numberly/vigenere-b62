import string

from vigenereb62 import encode, iter_reverse_digits


def test_iter_reverse_digits():
    assert list(iter_reverse_digits(12345, 10)) == [5, 4, 3, 2, 1]


def test_encode():
    size = 6
    b62 = [string.digits + string.ascii_letters] * size
    assert encode(b62, 0, size) == "000000"
    assert encode(b62, 10, size) == "a00000"
    assert encode(b62, 3844, size) == "001000"
    b_rand = ["kalqeimd"] * size
    assert encode(b_rand, 10) == "lakkkk"
