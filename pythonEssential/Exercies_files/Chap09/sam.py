class Animal:
    def __init__ (self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name
    
    def sound(self):
        return self._sound

def print_animal(o):
        if not isinstance(o, Animal):
            raise TypeError("object is not animal")
        print(o.type())
        print(o.name())
        print(o.sound())
        print('The {} is {} and says {}'.format(o.type(), o.name(), o.sound()))
def main():
    a0 = Animal("Cat", "Sam", "meow")
    print_animal(a0)
    b0 = Animal("Bird", "Robin", "Chipchip")
    print_animal(b0)

main()