import random

class HotelReservation:
    def __init__(self):
        self.booking = None

    def generate_id(self):
        return "HR" + str(random.randint(1000, 9999))

    def book_room(self):
        if self.booking:
            print("\nYou already have a booking. Cancel it first.\n")
            return

        name = input("Enter your name: ")
        contact = input("Enter your 10-digit contact number: ")

        if not (contact.isdigit() and len(contact) == 10):
            print("Invalid contact number.\n")
            return

        nights = int(input("Enter number of nights: "))

        print("\nAvailable Rooms:")
        print("1. Standard - ₹2000/night")
        print("2. Deluxe   - ₹3500/night")
        print("3. Suite    - ₹5000/night")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            room, price = "Standard", 2000
        elif choice == "2":
            room, price = "Deluxe", 3500
        elif choice == "3":
            room, price = "Suite", 5000
        else:
            print("Invalid room choice.\n")
            return

        total = nights * price

        print(f"\nBooking Summary:")
        print(f"Name: {name}")
        print(f"Contact: {contact}")
        print(f"Room: {room}")
        print(f"Nights: {nights}")
        print(f"Total Cost: ₹{total}\n")

        confirm = input("Confirm booking? (yes/no): ").lower()
        if confirm == "yes":
            self.booking = {
                "id": self.generate_id(),
                "name": name,
                "contact": contact,
                "room": room,
                "nights": nights,
                "total": total
            }
            print("\nBooking Confirmed!\n")
        else:
            print("\nBooking Cancelled.\n")

    def view_booking(self):
        if self.booking:
            print("\nYour Booking Details:")
            for k, v in self.booking.items():
                print(f"{k.capitalize()}: {v}")
            print()
        else:
            print("\nNo active booking.\n")

    def cancel_booking(self):
        if self.booking:
            confirm = input("Cancel booking? (yes/no): ").lower()
            if confirm == "yes":
                print(f"\nBooking {self.booking['id']} cancelled.\n")
                self.booking = None
            else:
                print("\nCancellation aborted.\n")
        else:
            print("\nNo booking found.\n")

    def menu(self):
        while True:
            print("===== HOTEL RESERVATION SYSTEM =====")
            print("1. Book a Room")
            print("2. View Booking")
            print("3. Cancel Booking")
            print("4. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                self.book_room()
            elif choice == "2":
                self.view_booking()
            elif choice == "3":
                self.cancel_booking()
            elif choice == "4":
                print("\nThank you for using Hotel Reservation System.\n")
                break
            else:
                print("\nInvalid choice.\n")

hotel = HotelReservation()
hotel.menu()
            

