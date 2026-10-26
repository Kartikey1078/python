# Encapsulation ka matlab hai data (variables) aur methods (functions) 
# ko ek class mein rakhna aur data ko controlled way mein access ya modify karna.


## Bad example of encapsulation
# class Bank:
#     def __init__(self,balance):
#         self.balance = balance

# obj = Bank(1000)

# obj.balance = -5000
# print(obj.balance)


## good Exaple of encapsulation 
class Bank:
    def __init__(self,bank_balance):
        self.__balance = bank_balance  # 1. Data hiding

    
    @property
    def balance(self):
        return self.__balance   # 2. Controlled reading
    
    @balance.setter
    def balance(self,amount):
        if amount >=0:
            self.__balance = amount    # 3. Validation
        else:
            print("Invalid amount")
        
obj = Bank(100)

# print(obj.balance)

# obj.balance = 2000
# print(obj.balance)

obj.balance = -500
print(obj.balance)