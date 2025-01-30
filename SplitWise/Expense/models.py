from Expense.Split.split import Split
from Expense.expense_split_type import ExpenseSplitType
from User.models import User

from typing import List

class Expense:
    def __init__(self, expense_id: str, expense_amount: float, description: str,
                 paid_by_user: User, split_type: ExpenseSplitType, split_details: List[Split]):
        self.expense_id = expense_id
        self.expense_amount = expense_amount
        self.description = description
        self.paid_by_user = paid_by_user
        self.split_type = split_type
        self.split_details = split_details


