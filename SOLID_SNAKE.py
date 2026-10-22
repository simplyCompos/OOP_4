from abc import ABC, abstractmethod


# ==========================================
# МОДЕЛЬ ТОВАРУ ТА ЗАМОВЛЕННЯ
# ==========================================

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# SRP: Order відповідає за дані замовлення.
class Order:
    def __init__(self, products):
        self.products = products

    def get_subtotal(self):
        return sum(product.price for product in self.products)


# ==========================================
# АБСТРАКЦІЇ ТА РОЗРАХУНКИ
# ==========================================

# OCP: можна додавати нові правила знижок.
class DiscountPolicy(ABC):
    @abstractmethod
    def calculate(self, subtotal):
        pass


class LoyaltyDiscount(DiscountPolicy):
    def calculate(self, subtotal):
        return subtotal * 0.10 if subtotal >= 3000 else 0


# OCP: можна замінити алгоритм доставки.
class DeliveryCalculator(ABC):
    @abstractmethod
    def calculate(self, subtotal):
        pass


class StandardDelivery(DeliveryCalculator):
    def calculate(self, subtotal):
        return 0 if subtotal >= 2500 else 120


# ==========================================
# ФОРМУВАННЯ ЧЕКА
# ==========================================

# SRP: тільки формує та виводить чек.
class ReceiptPrinter:
    def print_receipt(self, order, discount, delivery):
        print("Чек замовлення:")

        for product in order.products:
            print(f"{product.name} — {product.price:.2f} грн")

        subtotal = order.get_subtotal()
        final_price = subtotal - discount + delivery

        print(f"Сума товарів: {subtotal:.2f} грн")
        print(f"Знижка: {discount:.2f} грн")
        print(f"Доставка: {delivery:.2f} грн")
        print(f"До сплати: {final_price:.2f} грн")


# ==========================================
# ЗБЕРЕЖЕННЯ ТА ПОВІДОМЛЕННЯ
# ==========================================

# ISP: окремий контракт для збереження.
class OrderStorage(ABC):
    @abstractmethod
    def save(self, order):
        pass


class ConsoleOrderStorage(OrderStorage):
    def save(self, order):
        print("Замовлення збережено.")


# ISP: окремий контракт для повідомлень.
class NotificationSender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class ConsoleNotificationSender(NotificationSender):
    def send(self, message):
        print(message)


# ==========================================
# ОСНОВНИЙ СЕРВІС
# ==========================================

# DIP: сервіс працює з абстракціями,
# а конкретні об'єкти отримує через конструктор.
class ShopService:
    def __init__(
        self,
        discount_policy,
        delivery_calculator,
        receipt_printer,
        order_storage,
        notification_sender
    ):
        self.discount_policy = discount_policy
        self.delivery_calculator = delivery_calculator
        self.receipt_printer = receipt_printer
        self.order_storage = order_storage
        self.notification_sender = notification_sender

    def process_order(self, order):
        subtotal = order.get_subtotal()

        discount = self.discount_policy.calculate(subtotal)
        delivery = self.delivery_calculator.calculate(subtotal)

        self.receipt_printer.print_receipt(
            order, discount, delivery
        )

        self.order_storage.save(order)

        self.notification_sender.send(
            "Повідомлення клієнту відправлено."
        )


# ==========================================
# ЗАПУСК ПРОГРАМИ
# ==========================================

if __name__ == "__main__":
    products = [
        Product("Headphones", 1800),
        Product("Webcam", 1400),
        Product("Microphone", 900)
    ]

    order = Order(products)

    service = ShopService(
        LoyaltyDiscount(),
        StandardDelivery(),
        ReceiptPrinter(),
        ConsoleOrderStorage(),
        ConsoleNotificationSender()
    )

    service.process_order(order)
