from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPI(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class ShoppingCart:
    def __init__(self, payment):
        self.payment = payment

    def checkout(self, amount):
        self.payment.pay(amount)


if __name__ == "__main__":
    cart = ShoppingCart(UPI())
    cart.checkout(1000)