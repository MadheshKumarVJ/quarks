# python oops concepts
  ### Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects. Python supports OOP and provides features like encapsulation, inheritance, and polymorphism.

#### 1. **Classes and Objects:**
Classes are blueprints for objects, and objects are instances of classes.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.display_info())  # Output: 2020 Toyota Corolla
```

#### 2. **Encapsulation:**
Encapsulation restricts direct access to some of an object's components, which can prevent the accidental modification of data.

```python
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age  # Private attribute

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

# Creating an object of the Person class
person = Person("Alice", 30)
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30
```

#### 3. **Inheritance:**
Inheritance allows a class to inherit attributes and methods from another class.

```python
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__("Canis familiaris")
        self.name = name
        self.age = age

    def speak(self):
        return "Woof Woof"

# Creating an object of the Dog class
dog = Dog("Buddy", 3)
print(dog.speak())  # Output: Woof Woof
print(dog.species)  # Output: Canis familiaris
```

#### 4. **Polymorphism:**
Polymorphism allows methods to do different things based on the object it is acting upon, even if the method shares the same name.

```python
class Cat(Animal):
    def speak(self):
        return "Meow"

# Creating objects of Dog and Cat classes
animals = [Dog("Buddy", 3), Cat("Whiskers")]

for animal in animals:
    print(animal.speak())
# Output:
# Woof Woof
# Meow
```
