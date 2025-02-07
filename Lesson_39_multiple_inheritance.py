# multiple inheritance = inherit from more than one parent calss
#                        C(A, B)

# multilevel inheritance = inherit froma  parent which inherits from another parent
#                          C(B) <- B(A) <- A


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f" {self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")


# these do does not have the below attributes as they did not inherit it
rabbit.hunt()
hawk.flee()

