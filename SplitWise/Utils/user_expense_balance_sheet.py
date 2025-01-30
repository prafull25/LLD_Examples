from typing import Dict
from Utils.balance import Balance

class UserExpenseBalanceSheet:
    def __init__(self):
        self.user_vs_balance: Dict[str, Balance] = {}
        self.total_your_expense = 0.0
        self.total_you_owe = 0.0
        self.total_you_get_back = 0.0
        self.total_payment = 0.0

    def get_user_vs_balance(self) -> Dict[str, Balance]:
        return self.user_vs_balance

    def get_total_your_expense(self) -> float:
        return self.total_your_expense

    def set_total_your_expense(self, total_your_expense: float):
        self.total_your_expense = total_your_expense

    def get_total_you_owe(self) -> float:
        return self.total_you_owe

    def set_total_you_owe(self, total_you_owe: float):
        self.total_you_owe = total_you_owe

    def get_total_you_get_back(self) -> float:
        return self.total_you_get_back

    def set_total_you_get_back(self, total_you_get_back: float):
        self.total_you_get_back = total_you_get_back

    def get_total_payment(self) -> float:
        return self.total_payment

    def set_total_payment(self, total_payment: float):
        self.total_payment = total_payment
