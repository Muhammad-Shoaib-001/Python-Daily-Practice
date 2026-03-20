#Twentysecond program in Python

# x = "Hello, World"
# data = x.split(",")
# print(data)

# x = "Hello, World"
# data = x.rsplit(",")
# print(data)


# x = "Hello, World"
# data = x.splitlines(",")
# print(data)

# TwentyThird Program in Python

# x = "Hello, World"
# print(x.find("World"))

# x = "Hello, World"
# print(x.index("World"))

# email = "shoaibfaisal83@gmail.com"
# if email.endswith("@gmail.com"):
#     print("Gmail domain found")

# email = "shoaibfaisal83@gmail.com"
# if email.startswith("shoaib"):
#     print("User found")

#TwentyThird Program in Python

# email = "shoaibfaisal83@gmail.com"
# if email.count("@") <= 1:
#     print("valid email")

# TwentyForth Program in Python

# x = ["Hello","World"]
# print(" ".join(x))

# x = "25"
# print(x.isalpha())

# x = "25"
# print(x.isalnum())

# x = "25"
# print(x.isdigit())

# log = "ERROR:2026:database_failed"
# print(log.rsplit(":", 1))

# logs = "ERROR\nWARNING\nINFO"
# print(logs.splitlines())

# data = "Ali,24\nHaris,25\nSara,22"

# rows = data.splitlines()

# for row in rows:
#     print(row.split(","))

import pandas as pd

# df = pd.read_csv("data.csv")
# df = df.map(lambda x: x.upper() if isinstance(x,str) else x) for uppercase the values in the table 
# print(df)

# df = pd.read_csv("data.csv")
# df.columns = df.columns.str.upper()
# print(df)

# df = pd.read_csv("data.csv")
# print(df.head())

# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))

# class myclass():
#   def __len__(self):
#     return 0

# myobj = myclass()
# print(bool(myobj))


# x = 200
# print(isinstance(x, int))


# x = 15
# y = 4

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)
# print(x ** y)
# print(x // y)

# x = [1,2,3,4,5]

# if (count := len(x) > 3):
#     print(f"list has {count} elements")


# numbers = [1, 2, 3, 4, 5]

# if (count := len(numbers)) > 3:
#     print(f"List has {count} elements")