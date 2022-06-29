'''******Multiple Inheritance******'''

class employee:
    company = "Visa"
    eCode = 120


class freelancer:
    companny = "fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class programmer(employee, freelancer):
    name = "Jeet"

p = programmer()
p.upgradeLevel()
print(p.companny)  
print(p.level)
print(p.companny) 
