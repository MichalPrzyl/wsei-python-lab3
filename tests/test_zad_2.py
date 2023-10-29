from zad2 import Student


def test_constructor():
    p1 = Student(1, 2, 3, 4)
    assert p1.name == 1
    assert p1.phy == 2
    assert p1.chem == 3
    assert p1.bio == 4


def test_total_obtained():
    p1 = Student(1, 2, 3, 4)
    result = p1.total_obtained()
    assert result == 10

    p2 = Student(5, 4, 56, 21)
    result = p2.total_obtained()
    assert result == 5 + 4 + 56 + 21


def test_percentage():
    p1 = Student(1,3,5,8)  # 17
    assert p1.percentage() == 17 / 400

    p2 = Student(5, 4, 56, 21)  # 86
    assert p2.percentage() == 86/400
