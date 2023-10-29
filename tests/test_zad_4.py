from zad4 import Rectangle


def test_area_perimeter():
    r1 = Rectangle(1, 2)
    assert r1.area() == 2
    assert r1.perimeter() == 6

    r2 = Rectangle(3, 5)
    assert r2.area() == 15
    assert r2.perimeter() == 16
