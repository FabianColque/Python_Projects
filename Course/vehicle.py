 
class Vehicle:
    def __init__(self, model, brand) -> None:
        self.__model = model
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        self.__model = model
    
    def print(self):
        print(f'Brand: {self.__brand}')
        print(f'Model: {self.model}')


class Car(Vehicle):
    def __init__(self, model, brand, doors) -> None:
        super().__init__(model, brand)
        self.__doors = doors
    
    @property
    def doors(self):
        return self.__doors
    
    @doors.setter
    def doors(self, doors):
        self.__doors = doors

    def print(self):
        super().print()
        print(f'doors: {self.__doors}')


if __name__ == '__main__':
    car: Car = Car('Honda', 'Fit', 4)
    car.print()


        