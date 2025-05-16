class Employee:

    def __init__(self, name):
        self.name = name

class Departement:

    def __init__(self, employee):
        self.employee = employee 

emp = Employee("laiba")

dept = Departement(emp)
print(dept.employee.name)