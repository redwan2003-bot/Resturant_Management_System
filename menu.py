class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        item = MenuItem(name, price)
        self.items.append(item)
        print(f"Added {name} to the menu.")

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]
        print(f"Removed {name} from the menu.")

    def view_menu(self):
        print("Menu:")
        for item in self.items:
            print(f"{item.name}: ${item.price:.2f}")