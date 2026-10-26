## Abstraction ka matlab hai unnecessary internal details
#  ko hide karna aur user ko sirf zaroori functionality dikhana.
from abc import ABC,abstractmethod


class Bank(ABC):

    @abstractmethod
    def withdraw(self,amount):
        pass

class MyBank(Bank):
    def __init__(self,balance):
        self.balance = balance

    def withdraw(self,amount):
        if amount >=0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Invalid amount or insufficient balance") 

obj = MyBank(1000)
obj.withdraw(300)
print(obj.balance)
