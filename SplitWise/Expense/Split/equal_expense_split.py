from Expense.Split.expense_split import ExpenseSplit

class EqualExpenseSplit(ExpenseSplit):
    def validate_split_request(self, split_list, total_amount):
        amount_per_user = total_amount/len(split_list)

        for split in split_list:
            if split.get_amount_owe()!=amount_per_user:
                raise ValueError("The splits are not equal!")
