from abc import ABC , abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        print("Payment")
        pass
class CreditCardPayment(Payment):
    def pay(self,amount):
        print("Credit card",amount)
class UPIPayment(Payment):
    def pay(self,amount):
        print("UPI Payment",amount)
c=CreditCardPayment()
u=UPIPayment()
c.pay(1000)
u.pay(500)        