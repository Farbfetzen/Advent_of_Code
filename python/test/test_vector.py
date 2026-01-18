from src.util.vector import Vector2


def test__str__() -> None:
    assert str(Vector2(1, 2)) == "(1, 2)"


def test__repr__() -> None:
    assert repr(Vector2(1, 2)) == "V2(1, 2)"


def test__add__() -> None:
    assert Vector2(1, 2) + Vector2(3, 4) == Vector2(4, 6)


def test__iadd__() -> None:
    v = Vector2(1, 2)
    v += Vector2(-3, 4)
    assert v == Vector2(-2, 6)


def test__sub__() -> None:
    assert Vector2(1, 2) - Vector2(3, 5) == Vector2(-2, -3)


def test__isub__() -> None:
    v = Vector2(1, 2)
    v -= Vector2(-3, 4)
    assert v == Vector2(4, -2)


def test__lt__() -> None:
    # Automatically generated because order=True.
    assert Vector2(0, 1) < Vector2(1, 0)
    assert Vector2(1, 0) < Vector2(1, 1)


def test__le__() -> None:
    # Automatically generated because order=True.
    assert Vector2(0, 1) <= Vector2(1, 0)
    assert Vector2(1, 0) <= Vector2(1, 1)
    assert Vector2(0, 1) <= Vector2(0, 1)
    assert Vector2(1, 0) <= Vector2(1, 0)


def test__gt__() -> None:
    # Automatically generated because order=True.
    assert Vector2(1, 0) > Vector2(0, 1)
    assert Vector2(1, 1) > Vector2(1, 0)


def test__ge__() -> None:
    # Automatically generated because order=True.
    assert Vector2(1, 0) >= Vector2(0, 1)
    assert Vector2(1, 1) >= Vector2(1, 0)
    assert Vector2(1, 0) >= Vector2(1, 0)
    assert Vector2(1, 1) >= Vector2(1, 1)


def test_sort() -> None:
    """Vector2 should sort like tuples: Sorting by x and breaking ties by y.
    Sorting is automatically supported if a class has a __lt__ method.
    For Vector2 this is created because it's a dataclass with order=True.
    """
    v1 = Vector2(0, 1)
    v2 = Vector2(1, 1)
    v3 = Vector2(1, 0)
    v4 = Vector2(0, 1)
    # noinspection PyTypeChecker
    assert sorted([v1, v2, v3, v4]) == [v1, v4, v3, v2]


def test__iter__() -> None:
    for i, value in enumerate(Vector2(0, 1)):
        assert i == value

    # Unpacking should be possible if __iter__ is defined:
    x, y = Vector2(3, 7)
    assert x == 3
    assert y == 7


def test_turn_right() -> None:
    v = Vector2(1, 2).turn_right()
    assert v == Vector2(-2, 1)
    v = v.turn_right()
    assert v == Vector2(-1, -2)
    v = v.turn_right()
    assert v == Vector2(2, -1)
    v = v.turn_right()
    assert v == Vector2(1, 2)


def test_turn_left() -> None:
    v = Vector2(1, 2).turn_left()
    assert v == Vector2(2, -1)
    v = v.turn_left()
    assert v == Vector2(-1, -2)
    v = v.turn_left()
    assert v == Vector2(-2, 1)
    v = v.turn_left()
    assert v == Vector2(1, 2)


def test_above() -> None:
    assert Vector2(0, 0).above() == Vector2(0, -1)


def test_below() -> None:
    assert Vector2(0, 0).below() == Vector2(0, 1)


def test_left() -> None:
    assert Vector2(0, 0).left() == Vector2(-1, 0)


def test_right() -> None:
    assert Vector2(0, 0).right() == Vector2(1, 0)


def test_neighbors_4() -> None:
    top, right, bottom, left = Vector2(0, 0).neighbors_4()
    assert top == Vector2(0, -1)
    assert right == Vector2(1, 0)
    assert bottom == Vector2(0, 1)
    assert left == Vector2(-1, 0)


def test_manhattan_distance() -> None:
    assert Vector2(10, 20).manhattan_distance(Vector2(3, 7)) == 20
    assert Vector2(3, 7).manhattan_distance(Vector2(10, 20)) == 20
    assert Vector2(0, 0).manhattan_distance(Vector2(0, 0)) == 0
    assert Vector2(10, -3).manhattan_distance(Vector2(-3, 5)) == 21
