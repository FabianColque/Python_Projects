 
class Account:
    contador = 0

    def __init__(self, owner, salary, limit):
        self.__numero = Account.contador + 1
        self.__owner = owner
        self.__salary = salary
        self.__limit = limit
        Account.contador += 1

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        self.__salary = value
    
    @property
    def limit(self):
        return self.__limit        

    def extract(self):
        return f'Salary of {self.__salary} of client {self.__owner}'
    
    def deposit(self, value):
        self.__salary += value

    def getSalary(self, value):
        self.__salary -= value
    
    def transaction(self, value, destination):
        self.__salary -= value
        destination.__salary += value    


acc1 = Account('Fabian',  3000, 5000)
acc2 = Account('Ernesto', 2000, 4000)

print(acc1.extract())
#print(acc2.get_salary())
acc1.salary = 1000
print(acc1.__dict__)