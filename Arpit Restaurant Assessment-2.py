import random   

class RestaurantSystem:
    def __init__(self):
        self.menu = {
            1: {"name": "Pizza", "price": 300},
            2: {"name": "Burger", "price": 250},
            3: {"name": "Pasta", "price": 200},
            4: {"name": "Sandwich", "price": 270},
            5: {"name": "Coffee", "price": 250}
        }
        self.orders = []  
        self.next_order_id = 1001   
    def welcome(self):
        print("\n===========================================")
        print("     Welcome to Arpit's Restaurant")
        print("===========================================")

    def display_menu(self):
        print("\n------ MENU ------")
        print(f"{'Code':<6}{'Item':<12}{'Price (₹)':<10}")
        print("-----------------------------")
        for code, item in self.menu.items():
            print(f"{code:<6}{item['name']:<12}₹{item['price']:<10}")
        print("-----------------------------")

    def generate_order_id(self):
        order_id = self.next_order_id
        self.next_order_id += 1   
        return str(order_id)

    def take_order(self):
        order_items = []
        total_price = 0

        while True:
            code = input("\nEnter item code (0 to finish): ")
            if not code.isdigit():
                print("Please enter a valid number!")
                continue

            code = int(code)
            if code == 0:
                break
            if code not in self.menu:
                print("Invalid code! Try again.")
                continue

            qty = input(f"Enter quantity for {self.menu[code]['name']}: ")
            if not qty.isdigit() or int(qty) <= 0:
                print("Quantity must be a positive number!")
                continue

            qty = int(qty)
            price = self.menu[code]['price'] * qty
            order_items.append((self.menu[code]['name'], qty, price))
            total_price += price

        if order_items:
            order_id = self.generate_order_id()
            self.orders.append({"id": order_id, "items": order_items, "total": total_price})
            self.print_receipt(order_id, order_items, total_price)
        else:
            print("No items were ordered!")

    def print_receipt(self, order_id, order_items, total_price):
        print("\n==============================")
        print(f"Order Receipt - ID: {order_id}")
        print("==============================")
        for item in order_items:
            print(f"- {item[0]} x {item[1]} = ₹{item[2]}")
        print("------------------------------")
        print(f"Total Amount: ₹{total_price}")
        print("Thank you for your order!")
        print("==============================")

    def view_order(self):
        order_id = input("Enter Order ID to view: ").strip()

        for order in self.orders:
            if order["id"] == order_id:
                self.print_receipt(order_id, order["items"], order["total"])
                return
        print("Order not found!")

    def cancel_order(self):
        order_id = input("Enter Order ID to cancel: ").strip()

        for order in self.orders:
            if order["id"] == order_id:
                self.orders.remove(order)
                print(f"Order {order_id} has been canceled.")
                return
        print("Order not found!")

    def run(self):
        self.welcome()
        while True:
            print("\n===== RESTAURANT SYSTEM =====")
            print("1. Display Menu")
            print("2. Take Order")
            print("3. View Order")
            print("4. Cancel Order")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_menu()
            elif choice == "2":
                self.display_menu()
                self.take_order()
            elif choice == "3":
                self.view_order()
            elif choice == "4":
                self.cancel_order()
            elif choice == "5":
                print("Thank you for visiting Aryan's Restaurant! Goodbye")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    system = RestaurantSystem()
    system.run()
