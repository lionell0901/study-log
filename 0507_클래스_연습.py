class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f'{self.name} is barking')
    
my_dog = Dog('Buddy')
my_dog.bark()