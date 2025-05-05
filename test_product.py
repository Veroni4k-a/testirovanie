import pytest
from product import Product

# Фикстура для создания продукта, имитации сохранения и удаления из БД
@pytest.fixture
def product():
    # Создаем продукт с начальными значениями
    prod = Product("Товар", 100, "электроника")
    # Имитируем сохранение в БД
    prod.save_to_database()
    # Возвращаем объект для теста
    yield prod
    # Имитируем удаление из БД после теста
    prod.delete_from_database()

# Тест начального состояния продукта
def test_initial_state(product):
    assert product.name == "Товар"
    assert product.price == 100
    assert product.category == "электроника"
    assert product.discount == 0

# Параметризованный тест для установки скидки
@pytest.mark.parametrize("percent", [0, 10, 50, 100])
def test_set_discount(product, percent):
    product.set_discount(percent)
    assert product.discount == percent

# Параметризованный тест для расчета финальной цены
@pytest.mark.parametrize("price, discount, expected", [
    (100, 0, 100),
    (100, 10, 90),
    (200, 50, 100),
    (50, 100, 0),
    (100, 200, -100),
    (150.5, 20, 120.4),
])
def test_get_final_price(product, price, discount, expected):
    product.change_price(price)
    product.set_discount(discount)
    assert product.get_final_price() == pytest.approx(expected)

# Параметризованный тест для изменения цены
@pytest.mark.parametrize("new_price", [50, 0, -10, 150.5])
def test_change_price(product, new_price):
    product.change_price(new_price)
    assert product.price == pytest.approx(new_price)

# Тест метода get_description
def test_get_description(product):
    description = product.get_description()
    assert "Товар" in description
    assert "100 руб." in description
    assert "электроника" in description
    assert "0%" in description

    # Проверка с установленной скидкой
    product.set_discount(25)
    description = product.get_description()
    assert "25%" in description