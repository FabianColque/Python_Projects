
"""
Object Python -> Binarization
Binarization -> Object Python

Called by Serialization
"""

import pickle

class Animal:
    def __init__(self, name):
        self.__name = name

    def eat(self):
        print(f'{self.name} is eating')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f'{self._Animal__name} is wuau wuau')

cusco = Dog('Cusco')

#with open('animals.pickle', 'wb') as myfile:
#    pickle.dump(cusco, myfile)


#reading

with open('animals.pickle', 'rb') as myfile:
    cusco_reco = pickle.load(myfile)
    cusco_reco.speak()