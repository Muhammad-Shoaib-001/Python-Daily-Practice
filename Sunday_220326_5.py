# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# thislist = ["apple", "banana", "cherry"]
# i = 0 
# while i < len(thislist):
#     print(thislist[i])
#     i += 1

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# mylist = []

# for x in fruits:
#     if "a" in x :
#         mylist.append(x)
# print(mylist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in range(10)]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x.upper() for x in fruits]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# fruits.sort()
# print(fruits)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse=True)
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)

# def myfuc(n):
#     return abs(n - 50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key=myfuc)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# for x in list2 :
#     list1.append(x)
# print(list1)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)


# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# tuple1 = ("abc", 34, True, 40, "male")
# print(type(tuple1))

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)

