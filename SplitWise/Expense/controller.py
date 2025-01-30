from typing import List
from Utils.balance_sheet_controller import BalanceSheetController
from Expense.Split.split import Split
from Expense.Split.split_factory import SplitFactory
from Expense.models import Expense
from Expense.expense_split_type import ExpenseSplitType
from User.models import User
from Expense.models import Expense


class ExpenseController:
    def __init__(self):
        self.balance_sheet_controller = BalanceSheetController()

    def create_expense(self, expense_id: str, description: str, expense_amount: float,
                       split_details: List[Split], split_type: ExpenseSplitType, paid_by_user: User) -> Expense:
        expense_split = SplitFactory.get_split_object(split_type)
        expense_split.validate_split_request(split_details, expense_amount)

        expense = Expense(expense_id, expense_amount, description, paid_by_user, split_type, split_details)

        self.balance_sheet_controller.update_user_expense_balance_sheet(paid_by_user, split_details, expense_amount)

        return expense
