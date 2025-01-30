from Expense.expense_split_type import ExpenseSplitType
from Expense.Split.equal_expense_split import EqualExpenseSplit
from Expense.Split.percentage_expense_split import PercentageExpenseSplit
from Expense.Split.unequal_expense_split import UnequalExpenseSplit
class SplitFactory:
    @staticmethod
    def get_split_object(split_type : ExpenseSplitType):
        if split_type == ExpenseSplitType.EQUAL:
            return EqualExpenseSplit()
        elif split_type== ExpenseSplitType.UNEQUAL:
            return UnequalExpenseSplit()
        elif split_type == ExpenseSplitType.PERCENTAGE:
            return PercentageExpenseSplit()
        else:
            None

