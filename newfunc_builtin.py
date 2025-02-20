# ss = [1,2,3,4,4,5,6,10]
# maxx = []
# for i in range(len(ss)-1):
#     if ss[i] > ss[i + 1]:
#         maxx.append(ss[i])
# print(maxx)
# -------------------------------------------------max--------------------------------------------
# ss = [10,2,3,4,4,50,6,10,11]
# max=[]
# maxx = ss[0]
# for i in ss:
#     if i > maxx:
#         maxx = i
# print(maxx)
# -------------------------------------------------shop simple eskiz--------------------------------------------
# products = {
#     "apple": {"price": 10_000, "quantity": 50},
#     "banana": {"price": 12_000, "quantity": 30},
#     "orange": {"price": 15_000, "quantity": 40},
# }
# def changing(ss , name , price1 , quanlity1):
#     """changing for product"""
#     if name in ss:
#         # ss.update({f"{name}": {"price": {price1}, "quantity": {quanlity1}}})
#         ss[name]["price"] = price1
#         ss[name]["quantity"] = quanlity1
#         return f"{ss}"
#
# def sell_prodeuct(ss , name , quanlity11):
#     """sell product"""
#     if name in ss:
#         ss[name]["quantity"] -= quanlity11
#         return ss
#     else:
#         return f"\n{name} Maxsuloti yo'q , iltimos boshqa mahsulotni harid qiling \n{ss}"
# print(changing(products , "banana" , 12_000 , 12))
# print(sell_prodeuct(products , "appe" , 1))

# -------------------------------------------------life--------------------------------------------
# class Stack:
# #     def __init__(self):
# #         self.stack = []
# #
# #     def size(self):
# #         return len(self.stack)
# #
# #     def push(self, item):
# #         self.stack.append(item)
# #     def peek(self):
# #         if not self.is_empty():
# #             return self.stack[-1]
# #         else:
# #             return "empty"
# #     def pop(self):
# #         if not self.is_empty():
# #             return self.stack.pop()
# #         else:
# #             return "empty"
# #
# #
# #
# #     def is_empty(self):
# #         return len(self.stack) == 0
# #
# #
# #
# #
# #
# # s = Stack()
# # s.push(10)
# # s.push(20)
# # s.push(30)
# #
# # print(s.peek())
# # print(s.pop())
# # print(s.pop())
# # print(s.is_empty())
# # print(s.size())


# -------------------------------------------------------------------------------------------------


class Stack:
    """"@!@@!"""
    def __init__(self):
        self.cnt = 0
    def aa1(self , val):
        """@!@!@"""
        for i in val:
            if i == "(":
                self.cnt+=1
                print(self.cnt)
            elif i == ")":
                self.cnt-=1
                print(self.cnt)
        if self.cnt == 0:
            return "Hammasi to'gri"
        else:
            return "Hatolik bor"

