#task1.py

"""Write a program that outputs “even” if a number is even and “odd” if a number is odd. 
Think about what if the value is neither even nor odd 
(the value can be fractional or it can even not be a number at all)."""

while True:
    try:
        answer = float(input("What is your number?: "))
        if answer % 2 == 0:
            print("Even number.")
        else:
            print("Odd number.")
    except ValueError:
        print("That's not a number.")
