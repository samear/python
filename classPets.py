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
"""
example:
>>> from classPets import Pet
>>> polly = Pet("Polly", "Parrot")
>>> print("Polly is a", polly.getSpecies())
Polly is a Parrot
>>> print("Polly is a", Pet.getSpecies(polly))
Polly is a Parrot
>>> print("Polly is a", Pet.getSpecies())
Traceback (most recent call last):
  File "", line 1, in
TypeError: unbound method getSpecies() must be called with Pet instance as first
argument (got nothing instead)
"""