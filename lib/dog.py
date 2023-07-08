#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name= None, breed = None):
        if(name != None):
            if(type(name) == str):
                if( 1 < len(name) < 25):
                    print(f'Setting name to {name}.')
                    self._name = name
                else:
                    print("Name must be string between 1 and 25 characters.")
            else:
                print("Name must be string between 1 and 25 characters.")
        if(breed != None):
            loacted = False
            for breeds in APPROVED_BREEDS:
                if(breed == breeds):
                    self._breed = breed
                    loacted = True
            if (loacted == False):
                print("Breed must be in list of approved breeds.")
                
        

    def get_name(self):
        print("Retrieving name.")
        return self._name
    
    def get_breed(self):
        return self._breed
    
    name = property(get_name,__init__)
    breed = property(get_breed,__init__)