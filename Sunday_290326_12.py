# def my_function(fruits):
#   for fruit in fruits:
#     print(fruit)

# my_fruits = ["apple", "banana", "cherry"]
# my_function(my_fruits)

# def my_function(person):
#   print("Name:", person["name"])
#   print("Age:", person["age"])

# my_person = {"name": "Emil", "age": 25}
# my_function(my_person)

# def my_function(x, y):
#   return x + y

# result = my_function(5, 3)
# print(result)

# def func():
#     return ['apple','banana','cherry']
# fruits = func()
# print(fruits)
# print(fruits[1])
# print(fruits[2])

# def func():
#     return ['1','2']
# num = func()
# print(num[1])
# print(num[0])

# def my_function(name, /):
#   print("Hello", name)

# my_function("Emil")

# def my_function(name):
#   print("Hello", name)

# my_function(name = "Emil")

# def my_function(name, /):
#   print("Hello", name)

# my_function(name = "Emil")

# def my_function(*, name):
#   print("Hello", name)

# my_function(name = "Emil")   

# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))

# nums = [1, 2, 3, 4]
# result = list(map(lambda x: x * 2, nums))
# print(result) 

# nums = [1, 2, 3, 4, 5]
# even = list(filter(lambda x: x % 2 == 0, nums))
# print(even) 

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))


# def myfunc(n):
#   return lambda a : a * n

# result= myfunc(5)
# print(result(2))



# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))

# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# print(odd_numbers)

# students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
# sorted_students = sorted(students, key=lambda x: x[1])
# print(sorted_students)

# words = ["apple", "pie", "banana", "cherry"]
# sorted_words = sorted(words, key=lambda x: len(x))
# print(sorted_words)