# import mymodule

# mymodule.greetings("Shoaib")

# import module as mm

# a = mm.person1["age"]
# print(a)

# import platform

# x = platform.system()
# print(x)


# import platform
# x = dir(platform)
# print(x)

# from module import person1

# print(person1["age"])


# import datetime

# x = datetime.datetime.now()
# print(x)
# import datetime

# x = datetime.datetime.now()

# print(x.year)
# print(x.month)
# print(x.strftime("%Y-%y-%I-%A"))

# import datetime

# x = datetime.datetime(2020, 5, 17)

# print(x)

# import datetime

# x = datetime.datetime(2018, 6, 1)

# print(x.strftime("%B"))

# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)

# x = abs(-7.25)

# print(x)


# x = pow(4, 3)

# print(x)


# import math

# x = math.sqrt(64)

# print(x)

# import math

# x = math.ceil(1.4)
# y = math.floor(1.4)

# print(x) # returns 2
# print(y) # returns 1

# import math

# x = math.ceil(1.4)
# y = math.floor(1.4)

# print(x) # returns 2
# print(y) # returns 1


# import math

# x = math.pi

# print(x)

# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])

# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)

# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x))


# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x, indent=4, sort_keys=True))