
class Animal:
    def __init__(self, name) -> None:
        self.__name = name

    def speak(self):
        raise NotImplemented('Class chilld must to implement this method')
    
    def eat(self):
        print(f'{self.__name} is eating')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def speak(self):
        print(f'{self._Animal__name} speak wuau wuau')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def speak(self):
        print(f'{self._Animal__name} speaks miau miau')

class Rat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def speak(self):
        print(f'{self._Animal__name} speaks rat rat')

felix = Cat('Felix')
felix.speak()
felix.eat()

pluto = Dog('Pluto')
pluto.speak()
pluto.eat()

mickey = Rat('Michey')
mickey.speak()
mickey.eat()