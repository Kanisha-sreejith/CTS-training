from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):
    def pay(self):
        print("Paid using UPI")


class Card(Payment):
    def pay(self):
        print("Paid using Card")


class PaymentService:
    def process_payment(self, payment):
        payment.pay()


if __name__ == "__main__":
    service = PaymentService()
    service.process_payment(UPI())
    service.process_payment(Card())