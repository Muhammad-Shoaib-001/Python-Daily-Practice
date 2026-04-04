# while True: print(eval(input(">>>")))

# x = int(input("Number which you want table for :"))
 
# for y in range(1,11):
#         print(f"{x} x {y} =", x * y )

# Regular function (Restaurant style) - returns ALL at once
# def get_numbers():
#     return [1, 2, 3, 4, 5]  # Makes all 5 numbers at once

# result = get_numbers()
# print(result)
# # Generator (Vending machine style) - yields ONE at a time
# def get_numbers():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# result = get_numbers()

# print(next(result))  # 1
# print(next(result))  # 2
# print(next(result))  # 3
# print(next(result))  # 4
# print(next(result))  # 

# def get_numbers():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# for num in get_numbers():
#     print(num)  # Prints 1,2,3,4,5 each on new line

# Regular list - uses LOTS of memory (stores all 1 million numbers)
# def million_numbers_list():
#     return [i for i in range(1000000)]  # Stores everything at once
#     # Memory: ~28 MB

# # Generator - uses almost NO memory (stores only ONE number at a time)
# def million_numbers_generator():
#     for i in range(1000000):
#         yield i  # Creates and gives ONE number at a time
#     # Memory: ~28 bytes!

# result = million_numbers_generator()
# print(next(result))
# print(next(result))

# print(list(range(5)))
# print(list(range(1, 6)))
# print(list(range(5, 20, 3)))

# r = range(10)
# print(r[2])
# print(r[:3])


# r = range(0, 10, 2)
# print(6 in r)
# print(7 in r)

# r = range(0, 10, 2)
# print(len(r))

cars = ["Ford", "Volvo", "BMW"]
# x = cars[1]
# print(x)

# x = len(cars)
# print(x)

# cars.append("Honda")
# print(cars)

# cars.pop(1)
# print(cars)

# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# mystr = "banana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

