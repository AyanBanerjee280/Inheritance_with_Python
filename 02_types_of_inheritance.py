''' Types of inheritance
1) Single inheritance
Single inheritance occurs when child class inherits a single parent class
2)Multiple Inheritance
3)Multilevel inheritance'''

#***********Single Inheritance*********


class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an Employee")


class Programmer(Employee):
    language = "python"
    company = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is a Programmer")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)



