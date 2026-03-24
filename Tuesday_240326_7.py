# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018

# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# a = 5
# b = 2
# if a > b: print("a is greater than b")

# a = 2
# b = 330
# print("A") if a > b else print("B")

# a = 10
# b = 20
# bigger = a if a > b else b
# print("Bigger is", bigger)

# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

# temperature = 25
# is_raining = False
# is_weekend = True

# if (temperature > 20 and not is_raining) or is_weekend:
#   print("Great day for outdoor activities!")


# x = 41

# if x > 10:
#   print("Above ten,",end= " ")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")

# score = 85
# attendance = 90
# submitted = True

# if score >= 60:
#   if attendance >= 80:
#     if submitted:
#       print("Pass with good standing")
#     else:
#       print("Pass but missing assignment")
#   else:
#     print("Pass but low attendance")
# else:
#   print("Fail")

# username = "Emil"
# password = "python123"
# is_active = True

# if username:
#   if password:
#     if is_active:
#       print("Login successful")
#     else:
#       print("Account is not active")
#   else:
#     print("Password required")
# else:
#   print("Username required")

# a = 33
# b = 200

# if b > a:
#   pass

# age = 16

# if age < 18:
#   pass # TODO: Add underage logic later
# else:
#   print("Access granted")

# value = 50

# if value < 0:
#   print("Negative value")
# elif value == 0:
#   pass # Zero case - no action needed
# else:
#   print("Positive value")

# day = 4
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")

# day = 4
# match day:
#   case 6:
#     print("Today is Saturday")
#   case 7:
#     print("Today is Sunday")
#   case _:
#     print("Looking forward to the Weekend")

# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5:
#     print("Today is a weekday")
#   case 6 | 7:
#     print("I love weekends!")

# month = 5
# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5 if month == 4:
#     print("A weekday in April")
#   case 1 | 2 | 3 | 4 | 5 if month == 5:
#     print("A weekday in May")
#   case _:
#     print("No match")