class Split:
    def __init__(self, user, amount_owe: float):
        self.user = user
        self.amount_owe = amount_owe

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_amount_owe(self):
        return self.amount_owe

    def set_amount_owe(self, amount_owe: float):
        self.amount_owe = amount_owe
