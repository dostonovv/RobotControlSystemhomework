class BudgetManager:
    """class Budget Manager"""
    def __init__(self,income , expense , balance , category_income,category_expense):
        """dunder method"""
        self.income = income
        self.expense = expense
        self.balance = balance
        self.category_income = []
        self.category_expense = []
    def add_income(self , amount :int, category , date):
        self.income += amount
        self.balance += amount
        self.category_income.append((category, date))
        return f"{amount} qo‘shildi. Jami daromad: {self.income}"
    def add_expense(self, amount, category, date):
        self.expense += amount
        self.balance-=amount
        self.category_expense.append((category, date))
        return f"{amount} qo‘shildi. Jami xarajat: {self.expense}"
    def get_balance(self):
        allls = self.income - self.expense
        return f"Your balance : {allls}"
    def get_expense_by_category(self , category):
        pass
    def get_top_expense_category(self):
        pass
    def save_to_file(self):
        pass
    def load_file(self):
        pass
