class Atm:
    
    

    #constructor
    "It is a magic method"
    """Constructor is a special function or method which will be executed when the object is created for the class and inside the constructor what ever we defined it will be executed """
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.machine_on = True
        self.menu()

    # def start(self):
    #     while self.machine_on
    #         self.menu()
    
    def menu(self):
        while self.machine_on:
            user_input = input(""" Welcome to SBI ATM
                            1. Enter 1 to create a pin
                            2. Enter 2 to Deposit Money
                            3. Enter 3 to Cash withdrawl
                            4. Enter 4 to Balance Check
                            5. Enter 5 to Exit \n""")
            
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit_money()
            elif user_input == "3":
                self.with_drawl()
            elif user_input == "4":
                self.balance_check()
            elif user_input == "5":
                self.machine_on = False
            else:
                print("Invalid choice, please try again.")
            
    
    def create_pin(self):
        self.pin = input("Enter your pin: \n")
        print("print created successfully")

    def deposit_money(self):
        temp = input("enter your pin: \n")
        if temp == self.pin:
            self.amount = int(input("Enter the amount: \n"))
            self.balance += self.amount
            print("Amount Deposited Successfully")
        else:
            print("Invalid pin")
            
    def with_drawl(self):
        
        temp = input("enter your pin: \n")
        if temp == self.pin:
            self.amount = int(input("Enter the amount: \n"))
            if self.amount < self.balance:
                self.balance -= self.amount
                print("Amount Withdrawl Successfully")
            else:
                print("You have Insufficient Balance")
        else:
            print("Invalid pin")
            
    def balance_check(self):
        temp = input("enter your pin: \n")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")
            
            
        
        
            
            
        

        

        
        
        
    