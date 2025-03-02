#Encapsulation
""" Encapsulation means hiding data using __menu like """
""" You can hide methods also in Encapsulation """


## you have getter and setter to access hideen data and methods
class Atm:
    
    #Instance variable
    """Instance variable is a variable which will be declared inside the constructor and outside the method"""
    """ Instance variable will be different for each object"""
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.machine_on = True
        self.__menu()

    # def start(self):
    #     while self.machine_on
    #         self.menu()
    
    def get__pin(self):
        return self.__pin
    
    
    def set__pin(self,new__pin):
        if type(new__pin) == str:
            self.__pin = new__pin
            print("pin changed")
        else:
            print("Not allowed")

        
    
    def __menu(self):
        # while self.machine_on:
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
        self.__pin = input("Enter your pin: \n")
        print("print created successfully")

    def deposit_money(self):
        temp = input("enter your pin: \n")
        if temp == self.__pin:
            self.amount = int(input("Enter the amount: \n"))
            self.__balance += self.amount
            print("Amount Deposited Successfully")
        else:
            print("Invalid pin")
            
    def with_drawl(self):
        
        temp = input("enter your pin: \n")
        if temp == self.__pin:
            self.amount = int(input("Enter the amount: \n"))
            if self.amount < self.__balance:
                self.__balance -= self.amount
                print("Amount Withdrawl Successfully")
            else:
                print("You have Insufficient Balance")
        else:
            print("Invalid pin")
            
    def balance_check(self):
        temp = input("enter your pin: \n")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid pin")
            
            
            
sbi = Atm()

            
            
        
        
            
            
        

        

        
        
        
    