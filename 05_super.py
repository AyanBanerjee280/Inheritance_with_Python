#Super class

# Parent-->child1-->child2


class person:
    country = "India"
    city = "Kolkata"
    company = "Amazon"

    def __init__(self):
        print("Initializing person...\n")
    

    def takeBreath(self):
        print("I am breathing....")

class employee(person):
    company = "Honda"

    def __init__(self):
         super().__init__()
         print("Initializing employee...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")


    def takeBreath(self):
        super().takeBreath()
        print("I am a programmer, I am breathing ++..")

class programmer(employee):
    company = "fiverr"
    

    def __init__(self):
        super().__init__()
        print("Initializing employee...\n")

    def takeBreath(self):
        super().takeBreath()
        print("Hellooooooooo..")

    def getSalary(self):
        print("No salary to proogrammers")

p = person()
p.takeBreath()

e = employee()
e.takeBreath()

pr = programmer()
pr.takeBreath()
