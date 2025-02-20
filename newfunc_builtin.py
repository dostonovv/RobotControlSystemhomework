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