#Create a class Employee and add salary and increment properties to it. 
#Write a method salaryAfterIncrement method with a property decorator with a setter which changes
#the value of increment based on the salary

# salaryAfterIncrement = salary * increment

class Employee:
    salary = 1000 
    increment = 1.5
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement) 
print(e.increment)
e.salaryAfterIncrement = 2000
print(e.salaryAfterIncrement)
print(e.increment)