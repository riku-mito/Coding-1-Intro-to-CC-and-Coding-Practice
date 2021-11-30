# Week 5 Task B.py

"""Implement a Caesar Cipher function that takes a string and shift amount,
 outputs the encrypted string.
- Input: hello word
- Shift by: 7
- Output: olssv dvysk"""

word = input("Enter a string to enrypt: ")
shift = int(input("Enter a shift amount: "))

for letter in word.lower():
    if letter.isalpha():
        value = ord(letter) + shift
        if value > 122:
            value = value - 26
        print(chr(value), end="")
    else:
        print(letter, end="")
print()
    
