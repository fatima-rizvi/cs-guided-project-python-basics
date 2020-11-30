"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
#Steps
#Split up the string into individual letters
#Iterate through every letter in the string
#Count the x's and o's
#Return true or false based on the conditions

def XO(txt):
    x = 0
    o = 0
    chars = list(txt)
    for char in chars:
        if char.lower() == "x":
            x += 1
        elif char.lower() == "o":
            o += 1
    
    if x == o :
        return True
    elif x == 0 and o == 0:
        return True
    else:
        return False

print(XO("ooxx")) # True
print(XO("xooxx")) # False
print(XO("ooxXm")) # True (Case insensitive)
print(XO("zpzpzpp")) # True (Returns True if no x and o)
print(XO("zzoo")) # False

