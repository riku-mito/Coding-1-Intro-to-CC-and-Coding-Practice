# Week 4 Task B Homework.py

"""Start with 4 words “comfortable”, “round”, “support”, “machinery”, 
return a list of all possible 2 word combinations. 
Example: ["comfortable round", "comfortable support", "comfortable machinery", .....]"""

wordList = input("Please input a list of words separated with a space. ").split(" ")

for x in wordList:
    for y in wordList:
        if x == y:
            pass
        else:
            print(x, y)
            
