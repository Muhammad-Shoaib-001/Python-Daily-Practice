# def my_function(title, *args, **kwargs):
#   print("Title:", title)
#   print("Positional arguments:", args)
#   print("Keyword arguments:", kwargs)

# my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# def myfunc(a,b,c):
#     return a + b + c
# number = [1,2,3]
# result = myfunc(*number)

# print(result)

# a = input("Hello, Please Provide your name")
# print(a)

# def my_function(fname, lname):
#   print("Hello", fname, lname)

# person = {"fname": "Emil", "lname": "Refsnes"}
# my_function(**person)

# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()

# myfunc()

# x = 300

# def myfunc():
#   print(x)

# myfunc()

# print(x)

# x = 300

# def myfunc():
#   x = 200
#   print(x)

# myfunc()

# print(x)

# def myfunc():
#   global x
#   x = 300
#   print(x)
# myfunc()

# print(x)

# x = 300

# def myfunc():
#   global x
#   x = 200

# myfunc()

# print(x)

# def myfunc1():
#   x = "Jane"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2()
#   return x

# print(myfunc1())

# x = "global"

# def outer():
#   x = "enclosing"
#   def inner():
#     x = "local"
#     print("Inner:", x)
#   inner()
#   print("Outer:", x)

# outer()
# print("Global:", x)

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# print(myfunction())

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# @changecase
# def otherfunction():
#   return "I am speed!"

# print(myfunction())
# print(otherfunction())

# def changecase(func):
#   def myinner(x):
#     return func(x).upper()
#   return myinner

# @changecase
# def myfunction(nam):
#   return "Hello " + nam

# print(myfunction("John"))

# def changecase(func):
#   def myinner(*args, **kwargs):
#     return func(*args, **kwargs).upper()
#   return myinner

# @changecase
# def myfunction(nam):
#   return "Hello " + nam

# print(myfunction("John"))

# def changecase(n):
#   def changecase(func):
#     def myinner():
#       if n == 1:
#         a = func().lower()
#       else:
#         a = func().upper()
#       return a
#     return myinner
#   return changecase

# @changecase(3)
# def myfunction():
#   return "Hello Linus"

# print(myfunction())


# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# def addgreeting(func):
#   def myinner():
#     return "Hello " + func() + " Have a good day!"
#   return myinner

# @changecase
# @addgreeting
# def myfunction():
#   return "Tobias"

# print(myfunction())

# def myfunction():
#   return "Have a great day!"

# print(myfunction.__name__)

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Have a great day!"

# print(myfunction.__name__)

# import functools

# def changecase(func):
#   @functools.wraps(func)
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Have a great day!"

# print(myfunction.__name__)