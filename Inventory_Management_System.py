class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self):
        return self.quantity * self.price


class Inventory:
    def __init__(self):
        self.items = []

    # Add item to list
    def add_item(self, name, quantity, price):
        self.items.append(Item(name, quantity, price))
        print("Item added!\n")

    # Update quantity
    def update_quantity(self, name, new_quantity):
        for item in self.items:
            if item.name == name:
                item.quantity = new_quantity
                print("Quantity updated!\n")
                return
        print("Item not found.\n")

    # Show all items
    def show_items(self):
        if not self.items:
            print("No items in inventory.\n")
            return

        print("\n--- Inventory Items ---")
        for item in self.items:
            print(f"Name: {item.name}")
            print(f"Quantity: {item.quantity}")
            print(f"Price: {item.price}")
            print(f"Total Value: {item.total_value()}\n")

    # Total inventory value
    def total_inventory_value(self):
        total = 0
        for item in self.items:
            total += item.total_value()
        print(f"Total Inventory Value: {total}\n")


# Main Program
inventory = Inventory()

while True:
    print("Inventory Management System")
    print("1. Add Item")
    print("2. Update Item Quantity")
    print("3. Show All Items")
    print("4. Total Inventory Value")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Item name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))
        inventory.add_item(name, quantity, price)

    elif choice == "2":
        name = input("Item name to update: ")
        new_quantity = int(input("New quantity: "))
        inventory.update_quantity(name, new_quantity)

    elif choice == "3":
        inventory.show_items()

    elif choice == "4":
        inventory.total_inventory_value()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.\n")
