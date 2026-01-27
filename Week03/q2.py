cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
print("Apple appears", cart.count("apple"), "times in the cart.")
print("Index of first milk is: ", cart.index("milk"))
cart.remove("apple")
last_item = cart.pop()
print("Last item removed from the cart:", last_item)
print("Is banana in the cart?", "banana" in cart)
print(cart)
