#inheritance

class Person:
    def __init__(self, name, surname, cpf) -> None:
        self.__name = name
        self.__cpf = cpf
        self.__surname = surname

    def full_name(self):
        return f'{self.__name} {self.__surname}'

class Cliente(Person):
    def __init__(self, name, surname, cpf, salary) -> None:        
        super().__init__(name, surname, cpf)
        self.__salary = salary

class Employee(Person):
    def __init__(self, name, surname, cpf, license) -> None:
        super().__init__(name, surname, cpf)
        self.__license = license

    def full_name(self):
        return f'Employee: {self.__license} Nome: {self._Person__name}'
    

empl : Employee = Employee('Noemi', 'Lapa', '321654789-10', 123)

print(empl.full_name())