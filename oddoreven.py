#!/usr/bin/python3

number = int(input("Enter the number: "))

remainder = number % 2
if (remainder == 0):
    print(number, "is even")
else:
    print(number, "is odd")

