class Product:
    def __init__(self, name, price, category="основная"):
        self.name = name
        self.price = price
        self.category = category
        self.discount = 0
        print(f"[INFO] Продукт '{self.name}' создан с ценой {self.price} руб. в категории '{self.category}'.")

    def set_discount(self, percent):
        print(f"[INFO] Установка скидки {percent}% на продукт '{self.name}'.")
        self.discount = percent

    def get_final_price(self):
        final = self.price * (1 - self.discount / 100)
        print(f"[INFO] Финальная цена продукта '{self.name}' после скидки: {final} руб.")
        return final

    def change_price(self, new_price):
        print(f"[INFO] Цена продукта '{self.name}' изменена с {self.price} на {new_price}.")
        self.price = new_price

    def save_to_database(self):
        print(f"[DB] Продукт '{self.name}' сохранён в базу данных.")

    def delete_from_database(self):
        print(f"[DB] Продукт '{self.name}' удалён из базы данных.")

    def get_description(self):
        return f"Название: {self.name}, Цена: {self.price} руб., Категория: {self.category}, Скидка: {self.discount}%"