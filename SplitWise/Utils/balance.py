class Balance:
    def __init__(self):
       self.amount_owe = 0
       self.amount_get_back = 0
  
    def get_amount_owe(self):
        return self.amount_owe
    
    def get_amount_get_back(self):
        return self.amount_get_back

    def set_amount_owe(self,amount_owe):
        self.amount_owe = amount_owe

    def set_amount_get_back(self,get_back_amount):
        self.amount_get_back = get_back_amount
