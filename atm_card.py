class ATMCard:
    def __init__(self,defPin,defBalance):
        self.defPin = defPin
        self.defBalance = defBalance

    def getDefaultPin(self):
        return self.defPin     

    def getDefaultBalance(self):
        return self.defBalance
             