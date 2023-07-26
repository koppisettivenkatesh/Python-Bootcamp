class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")


class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

def animal_sound_in_zoo(animal):
    animal.make_sound()    

dog = Dog()
cat= Cat()

animal_sound_in_zoo(dog)  
animal_sound_in_zoo(cat)  