# Week 3 A Homework

"""Make a function that takes two arguments (given name and family name), 
the second of which is optional. Print a greeting according to which arguments are provided.
Example output: “Hello Kenneth.” or “Hello there, Kenneth of Lim!”
 """

name, surname = input("Please input name and family name: \n").split(" ")
print("Hello", name, surname, "\n")