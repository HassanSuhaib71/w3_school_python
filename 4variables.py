x = 5
y = "John"
print(x)
print(y)


print("==========================================================================")

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

print("=================================CASTING=========================================")

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

print("=================================Get The Type=========================================")

x = 5
y = "John"
print(type(x))
print(type(y))

print("=================================Single or Double Quotes=========================================")

x = "John"
# is the same as
x = 'John'

print("=================================Case-Sensitive=========================================")

a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)


print("=================================1.2=========================================")
print("=================================Variable Names=========================================")

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal Variable Names

# 2myvar = "John"
# my-var = "John"
# my var = "John"


print("=================================Multi Words Variable Names=========================================")
print("=================================Camel Case=========================================")

myVariableName = "John"

print("=================================Pascal Case=========================================")

MyVariableName = "John"

print("=================================Snake Case=========================================")

my_variable_case = "John"


print("=================================1.3=========================================")
print("=================================Many Values to Multiple Variable=========================================")

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("=================================One Value to Multiple Variables=========================================")

x = y = z = "Orange"
print(x)
print(y)
print(z)

print("=================================Unpack a Collection=========================================")

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
