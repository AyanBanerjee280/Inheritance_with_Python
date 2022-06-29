# Parent-->child1-->child2

class person:
    country = "India"
    city = "Kolkata"
    company = "Amazon"
    

    def takeBreath(self):
        print("I am breathing....")

class employee(person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")


    def takeBreath(self):
        print("I am a programmer, I am breathing ++..")

class programmer(employee):
    company = "fiverr"

    def getSalary(self):
        print("No salary to proogrammers")

p = person()
p.takeBreath()
print(p.company)
print(p.country)
print(p.city)
e = employee()
print(e.company)
e.takeBreath()
pr = programmer()
print(pr.company)
pr.takeBreath()
