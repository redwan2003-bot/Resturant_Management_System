from menu import Menu
from order import Order
from customer import CustomerManager


def main():
    global order
    menu = Menu()
    customer_manager = CustomerManager()

    while True:
        print("\nRestaurant Management System")
        print("1. Add Menu Item")
        print("2. Add Quantity")
        print("3. Remove Menu Item")
        print("4. View Menu")
        print("5. Add Customer")
        print("6. View Customers")
        print("7. Create Order")
        print("8. View Order")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter menu item name: ")
            price = float(input("Enter menu item price: "))
            menu.add_item(name, price)
        elif choice == '2':
            name = input("Enter menu item name to remove: ")
            menu.remove_item(name)
        elif choice == '3':
            menu.view_menu()
        elif choice == '4':
            name = input("Enter customer name: ")
            customer_manager.add_customer(name)
        elif choice == '5':
            customer_manager.view_customers()
        elif choice == '6':
            order = Order()
            while True:
                item_name = input("Enter menu item name to add to order (or 'done' to finish): ")
                if item_name.lower() == 'done':
                    break
                for item in menu.items:
                    if item.name == item_name:
                        order.add_item(item)
                        print(f"Added {item_name} to order.")
                        break
                else:
                    print("Item not found in menu.")
        elif choice == '7':
            order.view_order()
        elif choice == '8':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()