

#import json
import jsonpickle

#ret = json.dumps(['product', {'PlayStation 5' : ('2TB', 'New', '220v', 4500)}])

#print(ret)


class Cat:
    def __init__(self, name, race):
        self.__name = name
        self.__race = race

    @property
    def name(self):
        return self.__name

    @property
    def race(self):
        return self.__race

felix = Cat('Felix', 'Criolla')
#print(felix.__dict__)

# ret = json.dumps(felix.__dict__)
# print(ret)

# ret = jsonpickle.encode(felix)
# print(ret)

# with open('felix.json', 'w') as file:
#     ret = jsonpickle.encode(felix)
#     file.write(ret)

with open('felix.json', 'r') as file:
    content = file.read()
    ret = jsonpickle.decode(content)
    print(ret)
    print(ret.name)