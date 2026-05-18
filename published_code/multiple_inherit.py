class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is Fleeing")

class Lion(Predator):
    def voice(self):
        print(f"{self.name} Roarsss!!")

class Deer(Prey):
    pass

class Hyena(Predator, Prey):
    pass

lion = Lion("King")
deer = Deer("Brian")
hyena = Hyena("Jack")


lion.eat()
hyena.sleep()
deer.flee()
lion.voice()
