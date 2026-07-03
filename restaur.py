menu ={
    "cold tea": 90,
    "cold coffee": 100,
    "chowmin":70
}
print("welcome to our restaurant!")
print("Menu:")
order_amount=0
if menu:
    for item, price in menu.items():
        print(f"{item}: {price}")
    order = input("Enter your order: ")
    if order in menu:
        order_amount += menu[order]
        print(f"Your total bill: {order_amount}")
    else:
        print("Sorry, we don't have that item.")





