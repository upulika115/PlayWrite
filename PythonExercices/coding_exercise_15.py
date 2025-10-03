# Initialize cart
ItemsInCart = 0


def add_to_cart(items_to_add):
    global ItemsInCart  # So we can modify the global variable

    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")

    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")

    ItemsInCart += items_to_add
    print(f"{items_to_add} items added. Total in cart: {ItemsInCart}")


# Example usage
try:
    add_to_cart(2)  # should work
    add_to_cart(-1)  # should raise an exception
except Exception as e:
    print(e)