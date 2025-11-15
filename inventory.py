item_names = []
item_prices = {}

while True:
    print("===== INVENTORY MENU =====")
    print("[1] Add Item")
    print("[2] Update Price")
    print("[3] Exit")

    choice = input("Choice: ")

  
    if choice == "1":
        name = input("\nEnter item name: ")

        
        if name in item_names:
            print("Item already exists! Cannot add duplicate.\n")
            continue

        
        try:
            price = float(input("Enter price: "))
        except ValueError:
            print("Invalid input! Price must be a number.\n")
            continue

        
        item_names.append(name)
        item_prices[name] = price

        print("Item added successfully!\n")

   
    elif choice == "2":
        name = input("\nEnter item name to update: ")

        if name in item_names:
           
            try:
                new_price = float(input("Enter new price: "))
            except ValueError:
                print("Invalid input! Price must be a number.\n")
                continue

            item_prices[name] = new_price
            print("Price updated successfully!\n")

        else:
            print("Item not found in the inventory.\n")
    elif choice == "3":
        print("Exiting system...")
        break
    else:
        print("Invalid option. Please try again.\n")