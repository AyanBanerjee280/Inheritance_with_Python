# inheritance and more on object oriented programming
# DRY --> do not repeat yourself

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
