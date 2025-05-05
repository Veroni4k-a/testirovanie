1)Установить зависимости:
pip install -r requirements.txt

2)Запуск теста:
pytest -v test_calculator.py > result.log #к первому заданию
pytest -v test_calculator_parametrize.py > result_2.log #к второму заданию
pytest -v test_product.py > result_3.log #к третьему заданию с фикстурами

Если не запускать тесты, то есть блокноты сохраненные с прошлым запуском.
