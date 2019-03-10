# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:53:32 2019
@author: sam
"""

class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

#subclass of Pet
class Dog(Pet):
    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats
    def chasesCats(self):
        return self.chases_cats

#subclass of Pet
class Cat(Pet):

    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def __str__(self):
        return self.hates_dogs
