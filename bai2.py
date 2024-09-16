class Animal:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)

class Bear(Mammal):
    def __init__(self, name):
        super().__init__(name)

class Gorilla(Mammal):
    def __init__(self, name):
        super().__init__(name)

class Lizard(Reptile):
    def __init__(self, name):
        super().__init__(name)

class Snake(Reptile):
    def __init__(self, name):
        super().__init__(name)
def test_zoo():
    mammal_instance = Mammal("Stella")
    print(mammal_instance.__class__.__bases__[0].__name__)
    print(mammal_instance.name)
    
    lizard_instance = Lizard("John")
    print(lizard_instance.__class__.__bases__[0].__name__)
    print(lizard_instance.name)

if __name__ == "__main__":
    test_zoo()

    