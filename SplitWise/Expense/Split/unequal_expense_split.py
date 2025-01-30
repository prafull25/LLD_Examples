from Expense.Split.expense_split import ExpenseSplit

class UnequalExpenseSplit(ExpenseSplit):
    def validate_split_request(self, split_list, total_amount):
        return super().validate_split_request(split_list, total_amount)

        