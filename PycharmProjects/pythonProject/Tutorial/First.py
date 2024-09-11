

#tuples #immutable
#only count and index, can only get info out of a tuple, nothing else

# numbers = (1,2,3)
# x, y, z = numbers
# print(x)

#dictionary

# customer = {
#     "name" : "Apurba",
#     "age" : 3,
#     "is_Married": False
# }
#
# print(customer)
# print(customer["name"])

#oop

# class Point:
#     def move(self, n):
#         print(f"move {n}")
#
#     #constructor
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p1 = Point(10,29)
# p1.move(20)
# print(p1.y)

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print("Hello World " + self.name)
#
# man = Person("Apurba")
# man.talk()


#inheritance

# class Mammal:
#     def walk(self):
#         print("Walking")
#
# class Dog(Mammal):
#     pass
# class Cat(Mammal):
#     def meow(self):
#         print("Shut up")
#
# suri = Cat()
# suri.walk()
# suri.meow()

#modules

#file with some python code
# import convertors
# convertors.mess()
#or
# import mess from convertors
# mess()

#packages

# directory/container for multiple modules
# for packages we go:
# import "folder/packagename".modulename.function

# Array addition and multiplication
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

sum_array = a + b         # Element-wise addition
product_array = a * b     # Element-wise multiplication
scalar_multiplication = a * 2  # Multiply every element by a scalar

print(sum_array)
print(product_array)
print(scalar_multiplication)
