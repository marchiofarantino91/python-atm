from atm_card import ATMCard

class Customer:
    def __init__(self,id,pin=1234,balance=10000):
        self.id =id
        self.pin=pin
        self.balance = balance
    def getCustID(self):
        return self.id
    def getCustPin(self):
        return self.pin
    def getCustBalance(self):           
        return self.balance
    def withdraw(self,nominal):
        self.balance -=nominal
    def deposit(self , nominal):
        self.balance += nominal         


 