try:

    products = {
        1: {"name": "Item 1", "price": 10},
        2: {"name": "Item 2", "price": 15},
        3: {"name": "Item 3", "price": 20},
        5: {"name": "Item 5", "price": 25},
        6: {"name": "Item 6", "price": 30},
        7: {"name": "Item 7", "price": 35},
        8: {"name": "Item 8", "price": 40},
        9: {"name": "Item 9", "price": 45},
    }

    user = None
    cart = {}

    while True:
        print("Menu:")
        print("1. Create account")
        print("2. Log in")
        print("3. Log out")
        print("4. Add item")
        print("5. Delete item")
        print("6. Change item")
        print("7. Add item to cart")
        print("8. View cart")
        print("9. Complete the purchase")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = {"username": username, "password": password}
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = {"username": username, "password": password}
        elif choice == "3":
            print("Exit")
        elif choice == "4":
            if user and user["username"] == "Admin" and user["password"] == "Admin":
                name = input("Enter the name of the item: ")
                price = float(input("Enter the price of the item: "))
                product_id = max(products.keys()) + 1
                products[product_id] = {"name": name, "price": price}
                print(f"Item '{name}' was added {product_id}.")
            else:
                print("Access denied. This option is only available for administrator")
        elif choice == "5":
            if user and user["username"] == "Admin" and user["password"] == "Admin":
                product_id = int(input("Enter item identifier that has to be deleted: "))
                if product_id in products:
                    del products[product_id]
                    print(f"Item{product_id} was deleted")
                else:
                    print("Item with this identifier was not found")
            else:
                print("Access denied. This option is only available for administrator")
        elif choice == "6":
            if user and user["username"] == "Admin" and user["password"] == "Admin":
                product_id = int(input("Enter item identifier that has to be changed: "))
                if product_id in products:
                    name = input("Enter new item name: ")
                    price = float(input("Enter new item price: "))
                    products[product_id] = {"name": name, "price": price}
                    print(f"Item {product_id} was changed")
                else:
                    print("Item with this identifier was not found")
            else:
                print("Access denied. This option is only available for administrator")
        elif choice == "7":
            if user:
                product_id = int(input("Enter item identifier that has to be added to cart: "))
                if product_id in products:
                    quantity = int(input("Enter quantity: "))
                    if product_id not in cart:
                        cart[product_id] = {"name": products[product_id]["name"], "quantity": quantity,
                                            "price": products[product_id]["price"]}
                    else:
                        cart[product_id]["quantity"] += quantity
                    print(f"Item '{products[product_id]['name']}' was added to cart")
                else:
                    print("Item with this identifier was not found")
            else:
                print("For adding items to cart you have to log in")
        elif choice == "8":
            print("Cart:")
            for item_id, item in cart.items():
                print(f"{item['name']} (x{item['quantity']}): {item['price']} грн.")
            total = sum(item["quantity"] * item["price"] for item in cart.values())
            print(f"Total: {total} грн.")
        elif choice == "9":
            if not cart:
                print("Cart is empty")
            else:
                total = sum(item["quantity"] * item["price"] for item in cart.values())
                print(f"To be paid: {total} грн.")
                print("Thanks for the purchase!")
                cart = []
        else:
            print("Incorrect selection. Try again")


except Exception as e:
    print(e)