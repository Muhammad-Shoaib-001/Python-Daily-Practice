# class Person:
#     def __init__(self,name,age=15):
#          self.name = name
#          self.age = age

#     def greet(self):
#          print("Hello, my name is " + self.name + " and my age is " + self.age)

# p1 = Person("Shoaib","24")
# p1.greet()

# class Person:
#     def __init__(self,name,age=15):
#          self.name = name
#          self.age = age

#     def greet(self):
#          print("Hello, my name is " + self.name + " and my age is " + self.age)


# p1 = Person(input(" Please enter your name "),input(" Please enter your age: "))
# p1.greet()

# class Person:
#     def __init__(self,name):
#         self.name = name

#     def printname(self):
#         print(self.name)

# p1 = Person("Shoaib")
# p1.printname()

# class Person:
#   def __init__(myobject, name, age):
#     myobject.name = name
#     myobject.age = age

#   def greet(abc):
#     print("Hello, my name is " + abc.name)

# p1 = Person("Emil", 36)
# p1.greet()

# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
    
#     def display_info(self):
#         print(f"{self.brand} {self.model} {self.year}")

# car1 = Car("Toyota","Corolla","2026")
# car1.display_info()

# class Person:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         return "Hello, " + self.name
    
#     def welcome(self):
#         message = self.greet()
#         print(message + "! Welcome to our website.")
    
# p1 = Person("Shoaib")
# p1.welcome()

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Emil", 36)

# print(p1.name)
# print(p1.age)

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

# car1 = Car("Toyota", "Corolla")

# print(car1.brand)
# print(car1.model)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Tobias", 25)
# print(p1.age)

# p1.age = 26
# print(p1.age)

# class Person:
#   species = "Human" # Class property

#   def __init__(self, name):
#     self.name = name # Instance property

# p1 = Person("Emil")
# p2 = Person("Tobias")

# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)

# class Person:
#   lastname = ""

#   def __init__(self, name):
#     self.name = name

# p1 = Person("Linus")
# p2 = Person("Emil")

# Person.lastname = "Refsnes"

# print(p1.lastname)
# print(p2.lastname)

# class Person:
#   def __init__(self, name):
#     self.name = name

# p1 = Person("Tobias")

# p1.age = 25
# p1.city = "Oslo"

# print(p1.name)
# print(p1.age)
# print(p1.city)

