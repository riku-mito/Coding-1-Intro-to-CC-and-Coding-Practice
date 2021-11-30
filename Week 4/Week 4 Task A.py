# Week 4 Task A Homework.py

"""Write a program that given a list of numbers, 
multiply all numbers in the list. 
Bonus for ignoring non-number element. 
Example: input: [1, 2, 3, 4], output: 24"""

inputList = input("Please enter a list of numbers, separating them with a space.\n").split(" ")
numList = [ x for x in inputList if x.isdigit() ]

product = 1
string = ""
for num in numList:
    product = product * int(num)
    if numList.index(num) == len(numList)-1:
        string = string + num + "="
    else:
        string = string + num + "*"
print(string + str(product)) 
