
class Animal:
    def __init__(self, name, specie) -> None:
        self.__name = name
        self.__specie = specie

    def faz_som(self, som):
        print(f'O {self.__name} fala {som}')

class Cat(Animal):
    def __init__(self, name, specie, race):
        super().__init__(name, specie)
        super().faz_som('uauauau')
        self.race = race

felix = Cat('Felix', 'Feline', 'Angora')
felix.faz_som('miau')