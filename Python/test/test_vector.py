import pytest

from src.util.vector import Vector2


@pytest.mark.parametrize("x, y", [(0, 0), (1, 2), (-1, -2)])
def test_valid_init(x: int, y: int) -> None:
    v = Vector2(x, y)
    assert v.x == x and v.y == y


# noinspection PyArgumentList, PyTypeChecker
def test_invalid_init() -> None:
    with pytest.raises(TypeError) as exception:
        Vector2()
    assert str(exception.value) == "Vector2.__init__() missing 2 required positional arguments: 'x' and 'y'"

    with pytest.raises(TypeError) as exception:
        Vector2(1)
    assert str(exception.value) == "Vector2.__init__() missing 1 required positional argument: 'y'"

    with pytest.raises(TypeError) as exception:
        Vector2(0.1, 2.3)
    assert str(exception.value) == "x and y must be integers, got x=float, y=float"


def test_str() -> None:
    assert str(Vector2(1, 2)) == "(1, 2)"


def test_add() -> None:
    assert Vector2(1, 2) + Vector2(3, 4) == Vector2(4, 6)


# noinspection PyTypeChecker
def test_add_not_implemented() -> None:
    with pytest.raises(TypeError) as exception:
        _ = Vector2(1, 2) + (1, 2)
    assert str(exception.value) == "unsupported operand type(s) for +: 'Vector2' and 'tuple'"


def test_iadd() -> None:
    v = Vector2(1, 2)
    v += Vector2(-3, 4)
    assert v == Vector2(-2, 6)


def test_iadd_not_implemented() -> None:
    v = Vector2(1, 2)  # NOSONAR
    with pytest.raises(TypeError) as exception:
        v += (1, 2)
    assert str(exception.value) == "unsupported operand type(s) for +=: 'Vector2' and 'tuple'"


def test_sub() -> None:
    assert Vector2(1, 2) - Vector2(3, 5) == Vector2(-2, -3)


# noinspection PyTypeChecker
def test_sub_not_implemented() -> None:
    with pytest.raises(TypeError) as exception:
        _ = Vector2(1, 2) - (1, 2)
    assert str(exception.value) == "unsupported operand type(s) for -: 'Vector2' and 'tuple'"


def test_isub() -> None:
    v = Vector2(1, 2)
    v -= Vector2(-3, 4)
    assert v == Vector2(4, -2)


def test_isub_not_implemented() -> None:
    v = Vector2(1, 2)  # NOSONAR
    with pytest.raises(TypeError) as exception:
        v -= (1, 2)
    assert str(exception.value) == "unsupported operand type(s) for -=: 'Vector2' and 'tuple'"


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
