import pytest
from calculator import Calculator

# Инициализация калькулятора перед каждым тестом
@pytest.fixture
def calc():
    return Calculator()

# Параметризованные тесты для сложения
@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-2, 7, 5),
    (0, 0, 0),
    (1.5, 2.5, 4.0),
    (-1.5, 1.5, 0.0),
    (1000000000, 1, 1000000001),
    (-1000000000, -1, -1000000001),
    (2, 3.0, 5.0),
    (2.0, 3, 5.0),
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected

# Параметризованные тесты для вычитания
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (3, 5, -2),
    (0, 0, 0),
    (1.5, 0.5, 1.0),
    (-1.5, -0.5, -1.0),
    (1000000000, 1, 999999999),
    (-1000000000, -1, -999999999),
])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected

# Параметризованные тесты для умножения
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (-2, -3, 6),
    (0.5, 0.4, 0.2),
    (-0.5, 0.4, -0.2),
    (1000000, 1000000, 1000000000000),
    (0, 5, 0),
    (5, 0, 0),
])
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected

# Параметризованные тесты для деления
@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (5, 2, 2.5),
    (-6, 3, -2),
    (1.5, 0.5, 3),
    (-1.5, 0.5, -3),
    (0, 5, 0),
    (0, -5, 0),
])
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected

# Тесты на обработку деления на ноль
@pytest.mark.parametrize("a, b", [
    (5, 0),
    (10, 0),
    (-10, 0),
])
def test_divide_by_zero(calc, a, b):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(a, b)

# Тесты на обработку неверных типов данных
@pytest.mark.parametrize("a, b", [
    ("2", 3),
    (5, "3"),
    ("2", "3"),
    ([], 2),
    ({"a": 1}, 2),
])
def test_invalid_types(calc, a, b):
    with pytest.raises(TypeError):
        calc.add(a, b)
    with pytest.raises(TypeError):
        calc.subtract(a, b)
    with pytest.raises(TypeError):
        calc.multiply(a, b)
    with pytest.raises(TypeError):
        calc.divide(a, b)