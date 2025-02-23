# import json
# class BudgetManager:
#     """class Budget Manager"""
#     def __init__(self , balance , data):
#         """d434"""
#         self.balance = balance
#         self.data = data if data else {}
#
#
#     def incomef(self , amount , date):
#         if isinstance(amount , int):
#             self.balance += amount
#             self.data.update({
#                 date: [{"type": "+", "amount": amount}]
#             })
#         else:
#             return "Type Error Bro"
#
#     def expenses(self, amount, date):
#         if isinstance(amount, int):
#             if amount < self.balance:
#                 self.balance -= amount
#                 if date not in self.data:
#                     self.data[date] = []
#                 self.data[date].append({"type": "-", "amount": amount})
#             else:
#                 return "Amount Error"
#         else:
#             return "Type Error, Amount = int() !!!!"
#     def balances(self):
#         """@!@!@"""
#         return (f"{self.balance}$ Balansingiz !")
#     def write_base(self):
#         """#@#@"""
#         with open("Data_finance.json" , "w") as file:
#             json.dump(self.data , file , indent=4)
#     def read_base(self):
#         with open("Data_finance.json", "r") as file:
#             data = json.load(file)
#
#         print(json.dumps(data, indent=4))
#
#
# budget = BudgetManager(balance=1000, data={})
#
#
# budget.incomef(500, "20.02.25")
#
#
# budget.expenses(300, "21.02.25")
#
# budget.expenses(300, "21.02.25")
# budget.expenses(300, "21.03.25")
#
#
# print(budget.balances())
# budget.write_base()