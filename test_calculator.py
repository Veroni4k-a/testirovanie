import pytest

# Импортируйте ваш класс Calculator из соответствующего модуля
from calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    # Тесты для сложения
    def test_add_integers(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(-1, -1) == -2

    def test_add_floats(self):
        assert self.calc.add(0.1, 0.2) == pytest.approx(0.3)
        assert self.calc.add(-0.5, 0.5) == 0

    def test_add_zero(self):
        assert self.calc.add(5, 0) == 5
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(-5, 0) == -5

    def test_add_mixed_types(self):
        assert self.calc.add(2, 3.0) == 5.0
        assert self.calc.add(2.0, 3) == 5.0

    # Тесты для вычитания
    def test_subtract_integers(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(3, 5) == -2
        assert self.calc.subtract(-1, -1) == 0

    def test_subtract_floats(self):
        assert self.calc.subtract(0.5, 0.3) == pytest.approx(0.2)
        assert self.calc.subtract(-0.5, -0.3) == pytest.approx(-0.2)

    def test_subtract_zero(self):
        assert self.calc.subtract(5, 0) == 5
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(0, 0) == 0

    # Тесты для умножения
    def test_multiply_integers(self):
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(-2, -3) == 6

    def test_multiply_floats(self):
        assert self.calc.multiply(0.5, 0.4) == pytest.approx(0.2)
        assert self.calc.multiply(-0.5, 0.4) == pytest.approx(-0.2)

    def test_multiply_zero(self):
        assert self.calc.multiply(5, 0) == 0
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.multiply(0, 0) == 0

    # Тесты для деления
    def test_divide_integers(self):
        assert self.calc.divide(6, 3) == 2
        assert self.calc.divide(5, 2) == 2.5
        assert self.calc.divide(-6, 3) == -2

    def test_divide_floats(self):
        assert self.calc.divide(1.5, 0.5) == 3
        assert self.calc.divide(-1.5, 0.5) == -3

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)

    def test_divide_zero_numerator(self):
        assert self.calc.divide(0, 5) == 0
        assert self.calc.divide(0, -5) == 0

    # Тесты для типов данных
    def test_invalid_types(self):
        with pytest.raises(TypeError):
            self.calc.add("2", 3)
        with pytest.raises(TypeError):
            self.calc.subtract(5, "3")
        with pytest.raises(TypeError):
            self.calc.multiply("2", "3")
        with pytest.raises(TypeError):
            self.calc.divide("6", 2)


"""
test_add_integers, test_add_floats, test_add_zero, test_add_mixed_types:
Проверяют работу метода add с различными типами и значениями.
test_subtract_integers, test_subtract_floats, test_subtract_zero:
Проверяют метод subtract.
test_multiply_integers, test_multiply_floats, test_multiply_zero:
Проверяют метод multiply.
test_divide_integers, test_divide_floats, test_divide_by_zero, test_divide_zero_numerator:
Проверяют метод divide, включая деление на ноль и нулевой числитель.
test_invalid_types:
Проверяет, что методы корректно обрабатывают ошибки типов данных.
"""