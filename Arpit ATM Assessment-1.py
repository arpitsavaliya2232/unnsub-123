class ATM:
    def __init__(self):
        self.name = None
        self.mobile = None
        self.pin = None
        self.balance = 0
        self.transactions = []

    def activate_card(self):
        print("\n=== ATM Card Activation ===")
        self.name = input("Enter full name: ").strip()

        while True:
            mobile = input("Enter 10-digit mobile number: ").strip()
            if mobile.isdigit() and len(mobile) == 10:
                self.mobile = mobile
                break
            print("Invalid mobile number. Please try again.")

        while True:
            pin1 = input("Create a 4-digit PIN: ").strip()
            pin2 = input("Re-enter PIN for verification: ").strip()
            if pin1 == pin2 and pin1.isdigit() and len(pin1) == 4:
                self.pin = pin1
                break
            print("PINs do not match or invalid. Try again.")

        while True:
            try:
                deposit = float(input("Enter initial deposit (min ₹1000): "))
                if deposit >= 1000:
                    self.balance = deposit
                    self.transactions.append(f"Initial Deposit: ₹{deposit}")
                    print(f"Card Activated Successfully! Current Balance: ₹{self.balance}")
                    break
                else:
                    print("Minimum deposit is ₹1000.")
            except ValueError:
                print("Invalid amount. Please enter a number.")

    def verify_pin(self):
        for _ in range(3):
            entered = input("Enter your 4-digit PIN: ").strip()
            if entered == self.pin:
                return True
            else:
                print("Incorrect PIN.")
        print("Too many failed attempts. Operation cancelled.")
        return False

    def change_pin(self):
        print("\n--- Change PIN ---")
        if not self.verify_pin():
            return
        while True:
            new_pin1 = input("Enter new 4-digit PIN: ").strip()
            new_pin2 = input("Re-enter new PIN: ").strip()
            if new_pin1 == new_pin2 and new_pin1.isdigit() and len(new_pin1) == 4:
                self.pin = new_pin1
                print("PIN changed successfully!")
                break
            print("PINs do not match or invalid. Try again.")

    def deposit(self):
        print("\n--- Deposit Money ---")
        if not self.verify_pin():
            return
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                self.balance += amount
                self.transactions.append(f"Deposited: ₹{amount}")
                print(f"Deposited ₹{amount}. Current Balance: ₹{self.balance}")
            else:
                print("Invalid deposit amount.")
        except ValueError:
            print("Please enter a valid number.")

    def withdraw(self):
        print("\n--- Withdraw Money ---")
        if not self.verify_pin():
            return
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount > 0:
                if amount <= 1000:
                    charge = 0
                elif amount <= 20000:
                    charge = 100
                elif amount <= 100000:
                    charge = 1000
                else:
                    charge = 2000

                total = amount + charge
                if total <= self.balance:
                    self.balance -= total
                    self.transactions.append(f"Withdrew ₹{amount} (Charge ₹{charge})")
                    print(f"Withdrawn ₹{amount} with ₹{charge} charge. Balance: ₹{self.balance}")
                else:
                    print("Insufficient balance to cover withdrawal and charges.")
            else:
                print("Invalid withdrawal amount.")
        except ValueError:
            print("Please enter a valid number.")

    def check_balance(self):
        print("\n--- Check Balance ---")
        if not self.verify_pin():
            return
        print(f"Current Balance: ₹{self.balance}")

    def view_transactions(self):
        print("\n--- Last 10 Transactions ---")
        if not self.verify_pin():
            return
        if not self.transactions:
            print("No transactions yet.")
        else:
            for t in self.transactions[-10:]:
                print("-", t)

    def menu(self):
        while True:
            print("\n=== ATM Main Menu ===")
            print("1. Change PIN")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. View Last 10 Transactions")
            print("6. Exit ATM")

            choice = input("Select an option (1-6): ").strip()
            if choice == "1":
                self.change_pin()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.check_balance()
            elif choice == "5":
                self.view_transactions()
            elif choice == "6":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option, try again.")

atm = ATM()
atm.activate_card()
atm.menu()
j