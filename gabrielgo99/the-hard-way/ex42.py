class Animal(object):
    pass


## Dog is a Animal
class Dog(Animal):

    def __init__(self, name):
        ##
        self.name = name

## Cat is a animal
class Cat(Animal):

    def __init__(self, name):
        ##
        self.name = name

## Person is object
class Person(object):

    def __init__(self, name):
        ##
        self.name = name

        ##
        self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ##??
        super(Employee, self).__init__(name)
        ##
        self.salary = salary

## Fis is-a object
class Fish(object):
    pass

## Salmon is a Fish
class Salmon(Fish):
    pass

##Halibut is a Fish
class Halibut(Fish):
    pass


## rover is a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## Frank is-a Employee
frank = Employee("Frank", 120000)

## Frank has a Pet
frank.pet = rover

## Flipper is-a fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## Harry is a Halibut
harry = Halibut()
    
