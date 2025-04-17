class Customer:
    def __init__(self, name):
        self.name = name

class CustomerManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, name):
        customer = Customer(name)
        self.customers.append(customer)
        print(f"Added customer: {name}")

    def view_customers(self):
        print("Customers:")
        for customer in self.customers:
            print(customer.name)