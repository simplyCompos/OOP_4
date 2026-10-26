# Базовий клас замовлення
class Order:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Замовлення електроніки
class ElectronicsOrder(Order):
    pass


# Замовлення одягу
class ClothingOrder(Order):
    pass


# Factory — створення замовлень
class OrderFactory:
    @staticmethod
    def create_order(order_type, name, price):
        if order_type == "1":
            return ElectronicsOrder(name, price)
        elif order_type == "2":
            return ClothingOrder(name, price)
        else:
            raise ValueError("Невідомий тип замовлення")


# Базовий клас стратегії доставки
class DeliveryStrategy:
    def calculate_cost(self):
        raise NotImplementedError


# Звичайна доставка
class StandardDelivery(DeliveryStrategy):
    def calculate_cost(self):
        return 50


# Експрес-доставка
class ExpressDelivery(DeliveryStrategy):
    def calculate_cost(self):
        return 150


# Клас магазину, який обробляє замовлення
class Shop:
    def __init__(self, name):
        self.name = name

    def process_order(self, order, delivery):
        delivery_cost = delivery.calculate_cost()
        total = order.price + delivery_cost

        print("\n--- Результат замовлення ---")
        print(f"Магазин: {self.name}")
        print(f"Замовлення: {order.name}")
        print(f"Ціна: {order.price} грн")
        print(f"Factory створила: {type(order).__name__}")
        print(f"Strategy обрала: {type(delivery).__name__}")
        print(f"Доставка: {delivery_cost} грн")
        print(f"Разом: {total} грн")


# Головна частина програми
def main():
    print("=== Мінісистема замовлень ===")

    name = input("Назва товару: ")

    try:
        price = float(input("Ціна товару (грн): "))

        if price <= 0:
            print("Помилка: ціна має бути більшою за нуль.")
            return

        print("\nТип замовлення:")
        print("1 — Електроніка")
        print("2 — Одяг")
        order_type = input("Ваш вибір: ")

        order = OrderFactory.create_order(
            order_type, name, price
        )

        print("\nСпосіб доставки:")
        print("1 — Звичайна (50 грн)")
        print("2 — Експрес (150 грн)")
        delivery_type = input("Ваш вибір: ")

        if delivery_type == "1":
            delivery = StandardDelivery()
        elif delivery_type == "2":
            delivery = ExpressDelivery()
        else:
            print("Помилка: невідомий спосіб доставки.")
            return

        shop = Shop("SmartShop")
        shop.process_order(order, delivery)

    except ValueError as error:
        print(f"Помилка введення: {error}")


if __name__ == "__main__":
    main()
