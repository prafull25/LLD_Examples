from Utils.user_expense_balance_sheet import UserExpenseBalanceSheet

class User:
    def __init__(self, user_id: str, user_name: str):
        self.user_id = user_id
        self.user_name = user_name
        self.user_expense_balance_sheet = UserExpenseBalanceSheet()

    def get_user_id(self) -> str:
        return self.user_id

    def get_user_expense_balance_sheet(self) -> UserExpenseBalanceSheet:
        return self.user_expense_balance_sheet