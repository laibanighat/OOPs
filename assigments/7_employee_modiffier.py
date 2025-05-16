class Employee:

    def __init__(self, name, salary, ssn):
        self.name = name #public
        self._salary = salary #protected
        self.__ssn = ssn #private 

emp = Employee("subhan" , 5000, "03293086256")


print(emp.name)
print(emp._salary)
# print(emp.__ssn)
print(emp._Employee__ssn)