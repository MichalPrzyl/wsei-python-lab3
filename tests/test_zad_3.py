from zad3 import Calculator


def test_constructor():
    c1 = Calculator(23, 42)
    assert c1.num1 == 23
    assert c1.num2 == 42


def test_add():
    c1 = Calculator(23, 42)
    assert c1.add() == 65

    c2 = Calculator(11, 23)
    assert c2.add() == 34

    c3 = Calculator(1, 2)
    assert c3.add() == 3

    c4 = Calculator(102, 23)
    assert c4.add() == 125


def test_subtract():
    c1 = Calculator(23, 42)
    assert c1.subtract() == 42 - 23

    c2 = Calculator(11, 23)
    assert c2.subtract() == 23 - 11

    c3 = Calculator(1, 2)
    assert c3.subtract() == 2 - 1

    c4 = Calculator(102, 23)
    assert c4.subtract() == 23 - 102


def test_multiple():
    c1 = Calculator(23, 42)
    assert c1.multiple() == 23 * 42

    c2 = Calculator(11, 23)
    assert c2.multiple() == 23 * 11

    c3 = Calculator(1, 2)
    assert c3.multiple() == 2 * 1

    c4 = Calculator(102, 23)
    assert c4.multiple() == 23 * 102


def test_div():
    c1 = Calculator(23, 42)
    assert c1.div() == 23 / 42

    c2 = Calculator(11, 23)
    assert c2.div() == 11 / 23

    c3 = Calculator(1, 2)
    assert c3.div() == 1 / 2

    c4 = Calculator(102, 23)
    assert c4.div() == 102 / 23

    # TODO: Test division by 0
    # c5 = Calculator(102, 0)
    # assert c4.div() == 0
