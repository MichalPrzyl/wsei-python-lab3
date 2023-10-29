def test_constructor():
    from zad1 import Point
    p1 = Point(1, 2, 3)
    assert p1.x == 1
    assert p1.y == 2
    assert p1.z == 3


def test_square_sum():
    from zad1 import Point
    p1 = Point(1, 2, 3)
    result = p1.square_sum()
    # 1 + 4 + 9 = 14
    assert result == 14


def test_square_sum_2():
    from zad1 import Point
    p1 = Point(5, 2, -1)
    result = p1.square_sum()
    # 25 + 4 + 1 = 30
    assert result == 30
