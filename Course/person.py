from datetime import date


class Person:
    def __init__(self, name, birthday, email) -> None:
        self.__name = name
        self.__birthday = birthday
        self.__email = email

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def birthday(self):
        return self.__birthday
    
    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email
    
    def print(self):
        print(f'Name: {self.name}')
        print(f'Birthday: {self.birthday}')
        print(f'Email: {self.email}')


if __name__ == '__main__':
    me = Person('Fabian', date(1992, 2, 19), 'fbcolque@gmail.com')
    me.print()