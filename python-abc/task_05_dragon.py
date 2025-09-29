#!/usr/bin/python3

class SwimMixin:
    def swim(self):
        print ("The creature is swimming!")

class FlyMixin:
    def fly(self):
        print ("The creature is flying!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon is roaring!")

dracon = Dragon()
dracon.swim()
dracon.fly()
dracon.roar()
