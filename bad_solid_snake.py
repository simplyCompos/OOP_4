class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShopManager:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        self.products.append(Product(name, price))

    def process_order(self):
        # Розрахунки
        subtotal = sum(p.price for p in self.products)

        discount = subtotal * 0.10 if subtotal >= 3000 else 0
        delivery = 0 if subtotal >= 2500 else 120

        final_price = subtotal - discount + delivery

        # Формування чека
        print("Чек замовлення:")

        for product in self.products:
            print(f"{product.name} — {product.price:.2f} грн")

        print(f"Сума товарів: {subtotal:.2f} грн")
        print(f"Знижка: {discount:.2f} грн")
        print(f"Доставка: {delivery:.2f} грн")
        print(f"До сплати: {final_price:.2f} грн")

        # Збереження та повідомлення
        print("Замовлення збережено.")
        print("Повідомлення клієнту відправлено.")


# Запуск початкової версії
if __name__ == "__main__":
    shop = ShopManager()

    shop.add_product("Headphones", 1800)
    shop.add_product("Webcam", 1400)
    shop.add_product("Microphone", 900)

    shop.process_order()
