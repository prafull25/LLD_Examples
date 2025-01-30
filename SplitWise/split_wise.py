from User.models import User
from Group.controller import GroupController
from Utils.balance_sheet_controller import BalanceSheetController
from Expense.Split.split import Split
from Expense.expense_split_type import ExpenseSplitType
from User.controller import UserController
from Group.models import Group

class Splitwise:

    def __init__(self):
        self.user_controller = UserController()
        self.group_controller = GroupController()
        self.balance_sheet_controller = BalanceSheetController()

    def example(self):
        self.setup_user_and_group()

        # Step 1: Add members to the group
        group = self.group_controller.get_group_by_group_id("1")
        group.add_member(self.user_controller.get_user_by_user_id("U0002"))
        group.add_member(self.user_controller.get_user_by_user_id("U0003"))

        # Step 2: Create an expense inside a group
        splits = []
        split1 = Split(self.user_controller.get_user_by_user_id("U0001"), 300)
        split2 = Split(self.user_controller.get_user_by_user_id("U0002"), 300)
        split3 = Split(self.user_controller.get_user_by_user_id("U0003"), 300)
        splits.extend([split1, split2, split3])
        group.create_expense("Exp1001", "Breakfast", 900, splits, ExpenseSplitType.EQUAL, self.user_controller.get_user_by_user_id("U0001"))

        splits2 = []
        splits2_1 = Split(self.user_controller.get_user_by_user_id("U0001"), 400)
        splits2_2 = Split(self.user_controller.get_user_by_user_id("U0002"), 100)
        splits2.extend([splits2_1, splits2_2])
        group.create_expense("Exp1002", "Lunch", 500, splits2, ExpenseSplitType.UNEQUAL, self.user_controller.get_user_by_user_id("U0002"))

        for user in self.user_controller.get_all_users():
            self.balance_sheet_controller.show_balance_sheet_of_user(user)

    def setup_user_and_group(self):
        # Onboard user to splitwise app
        self.add_users_to_splitwise_app()

        # Create a group by user1
        user1 = self.user_controller.get_user_by_user_id("U0001")
        self.group_controller.create_new_group( "Outing with Friends", user1)

    def add_users_to_splitwise_app(self):
        # Adding User1
        user1 = User("U0001", "User1")

        # Adding User2
        user2 = User("U0002", "User2")

        # Adding User3
        user3 = User("U0003", "User3")

        self.user_controller.add_user(user1)
        self.user_controller.add_user(user2)
        self.user_controller.add_user(user3)
