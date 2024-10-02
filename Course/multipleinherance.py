

# Direct Deviration 
class Base1:
    pass

class Base2:
    pass

class MultiDeri(Base1, Base2):
    pass

# No direct derivation
class Base1:
    pass

class Base2(Base1):
    pass

class MultiDeri(Base2):
    pass

#//////////

class Animal:
    def __init__(self, name) -> None:
        self.__name = name
    
    def compliment(self):
        return f'I am {self.__name}'
    
class Aquatic(Animal):
    def __init__(self, name):
        super().__init__(name)

    def swin(self):
        return f'{self._Animal__name} is swinning'
    
    def compliment(self):
        return f'I am {self._Animal__name} of the sea'
    
class Land(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def walk(self):
        return f'{self._Animal__name} is walking'
    
    def compliment(self):
        return f'I am {self._Animal__name} of the land'
    
class Penguim(Land, Aquatic):
    def __init__(self, name) -> None:
        super().__init__(name)

    
whale = Aquatic('Wally')
print(whale.swin())
print(whale.compliment())

tatu = Land('Xim')
print(tatu.walk())
print(tatu.compliment())

tux = Penguim('Tux')
print(tux.walk())
print(tux.swin())
print(tux.compliment())
