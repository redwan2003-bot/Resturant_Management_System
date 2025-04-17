class Order:
    def __init__(self):
        """

        :rtype: None
        """
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def view_order(self):
        print("Order:")
        for item in self.items:
            print(f"{item.name}: ${item.price:.2f}")
        total = sum(item.price for item in self.items)
        print(f"Total: ${total:.2f}")