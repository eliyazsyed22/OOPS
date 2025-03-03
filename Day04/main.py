# refernce variable
""" reference varibale means the object which you're creating to initilaise class it is called as reference variable """

# pass by reference


class Customer:
    
    def __init__(self,name):
        self.name = name
        
        
        
# def greet(customer):
    
#     if customer.gender == "Male":
#         print("Hello",customer.name,"sir")
#     else:
#         print("Hello",customer.name,"maam")
        
def greet(customer): 
    print(id(customer))
           
cust = Customer("Eliyaz")
# print(cust.name)

print(id(cust))

greet(cust)

