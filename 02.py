# print("---------------- Addition of 2 numbers program -----------------")
# a = input("Enter first number: ") # input("Prompt String: ")

# # Check type of data
# # type()
# # print(type(a))

# b = input("Enter second number: ")
# # print(type(b))


# # Explicit
# # a = int(a)
# # print("The type of a is ", type(a))

# # b = int(b)
# # print("The type of b is ", type(b))

# # print(a + b)
# # print(int(a) + int(b))
#c = int(a) + int(b)
# # print("The value of c is",c," with type", type(c))
# # print("The value of c is " + str(c))
# # Formatted Strings
#print(f"The value of c is {c} and type of c is {type(c)}")

# int, float, str, list, tuple, dict, set, complex, bool

# Convert one type into another type (Type Conversion)
# Implicit => Auto - Same category
# Explicit => int => float, int => str, str => float...


# Operators
# Used to perform certain operations of variables and values

# Arithmetic
# +, -, *, /, //, %, **

# Assignment
# =, +=, -=, *=, /=,%=, **=

# Comparision
# ==, !=, >, <, >=, <=

# Logical
# and, or, not

# Bitwise
# &, |, ~, ^, >>, <<

# Special
# Identity => is, is not
# Membership => in, not in


# ------------------ Decision Making / Conditional Statements ------------------
# Credit
# Debits
# Balance, Performance

# if, else, elif

# if => specified condition when met, execute the respective block of code
# # Number is positive, entered by user
# # Condition: It should be greater than zero (Comparing)
# num = int(input("Enter a number: "))
# print(num > 0)
# if num > 0:
#     print(f"{num} is positive number")

# # Number is positive or negative, entered by user
num = int(input("Enter a number: "))
print(num < 0)
if (num < 0) == False:
   print(f"{num} is positive number")
else:
   print(f"{num} is negative number")

# Number is positive or negative or zero, entered by user
# NESTED Approach
# num = int(input("Enter a number: "))
# if num > 0:
#     print(f"{num} is positive number")
# else:
#     if num == 0:
#         print(f"{num} is ZERO value")
#     else:
#         print(f"{num} is negative number")

# elif => If you have more than 2 conditions
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive number")
elif num < 0:
    print(f"{num} is negative number")
else:
    print(f"{num} is ZERO value")