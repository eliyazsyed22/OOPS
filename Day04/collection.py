#collection  of objects

class Customer:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def into(self):
        print("Iam",self.name,"and Iam",self.age)


c1 = Customer("Eliyaz",45)
c2 = Customer("gousiya",35)
c3 = Customer("john",22)

L = [c1,c2,c3]

for i in L:
    i.into()