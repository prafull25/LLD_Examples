from Expense.controller import ExpenseController
from Expense.models import Expense, ExpenseSplitType, Split
from User.models import User
from typing import List

class Group:
    _group_counter = 0
    def __init__(self):
        Group._group_counter += 1
        self.group_id = str(Group._group_counter)
        self.group_name: str = ""
        self.group_members: List[User] = []
        self.expense_list: List[Expense] = []
        self.expense_controller = ExpenseController()

    def add_member(self,member:User):
        self.group_members.append(member)

    def get_group_id(self):
        return self.group_id
    
    def set_group_name(self,name):
        self.group_name = name
    
    def create_expense(
        self, 
        expense_id: str, 
        description: str, 
        expense_amount: float, 
        split_details: List[Split], 
        split_type: ExpenseSplitType, 
        paid_by_user: User
    ) -> Expense:
        """Creates an expense and adds it to the group's expense list."""
        expense = self.expense_controller.create_expense(
            expense_id, description, expense_amount, split_details, split_type, paid_by_user
        )
        self.expense_list.append(expense)
        return expense