class Animal:
    def __init__ (self, type, name, sound):
        self._a = type
        self._b = name
        self._c = sound

    def type(self):
        return self._a

    def name(self):
        return self._b

    def sound(self):
        return self._c

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print("Type: ", o.type())
    print("Name: ", o.name())
    print("Sound: ", o.sound())
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

def main():
    a0 = Animal('Kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor', 'veronical', 'hello'))

    #pprint(isinstance(a0, car))

if __name__ == '__main__': main()
