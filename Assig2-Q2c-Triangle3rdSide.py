#OOP Assignment 2

'''c) Write a Python program to get the third side of right angled triangle from two given
sides. (5 marks)
'''
# import the math module  
import math            # So that we can use the sqrt() function
# Formula... h2 = l2 + b2

length=int(input("Enter the Length of the Trianle: "))
base=  int(input("Enter the  Base  of the Trianle: "))

l2=length ** 2         #Get the Square of the Length
b2=base ** 2           #Get the Square of the Base

h2=l2+b2               # Get the sum

h2 = math.sqrt(h2)     # Now get the Square Root

print(h2)
