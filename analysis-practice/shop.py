import os import sys items = [] def addItem(name,price): item={'name':name,'price':price}
items.append(item) def getTotalPrice(): total=0 for i in items: total=total+i['price'] return total def
printReceipt(): print("=== Чек ===") for i in items: print(i['name'], i['price']) s=getTotalPrice()
print("Итого:", s) addItem("Хлеб", 45) addItem("Молоко", 89) addItem("Масло", 120) printReceipt()
