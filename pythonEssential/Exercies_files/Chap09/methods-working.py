#!/usr/bin/env python3

class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'sam'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meeee000ow'

    def type(self, t = None):
            if t: self._type = t
            return self._type

    def name(self, n = None):
            if n: self._name = n
            return self._name

    def sound(self, s = None):
            if s: self._sound = s
            return self._sound

    def __str__(self):
            return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'
            
def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    b0 = Animal(type='cat', name='kitty', sound='mimi')
    print(a0)
    print(b0)
    #print(b0.sound('kwark'))

main()
if __name__ == '__main___': main()