# Riku Mito Week2 Task B.py

"""Given a string of text, print the number of times each letter in the alphabets a-z appear. Hint: “a” != “A”."""

string = input("Enter your text. ")

# Make the text lowercase
string = string.lower()
# Remove all spaces and non-alphabetical chars
string = ''.join([i for i in string if i.isalpha()])

# Declare list with 26 indexes for the 26 letters in the alphabet
alphabet = [0] * 26

# Loop through the letters in the string
for x in string:
    # Convert them into ASCII numbers and subtract by "a" (97)
    letter = ord(x) - 97
    # Add 1 to each corresponding letter
    alphabet[letter] = alphabet[letter] + 1

# For loop to print each letter 
for x in range(0,26):
    print(str(chr(97+x)) + ": " + str(alphabet[x]))
