inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8),
}
print("")
print("====== Current Inventory =======")
for item, (price, quantity) in inventory.items():
    print(f"Item: {item}, Price: ${price}, Quantity: {quantity}")
print("")
electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}
all_products = electronics | accessories

print("All products categories: ", all_products)

print("")
price_list = [item[0] for item in inventory.values()]
price_list.sort()
print("Sorted Prices: ", price_list)
print("Lowest Price: ", price_list[0])
print("Lowest Price: ", price_list[-1])

inventory["Headphones"] = (49.99, 20)

inventory["Mouse"] = (inventory["Mouse"][0], 12)

del inventory["Monitor"]

print("")
print("====== Final Inventory =======")
for item, (price, quantity) in inventory.items():
    print(f"Item: {item}, Price: ${price}, Quantity: {quantity}")
print("")
