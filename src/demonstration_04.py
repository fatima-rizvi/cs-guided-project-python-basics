"""
Challenge #4:

Create a function that takes length and width and finds the perimeter of a
rectangle.

Examples:
- find_perimeter(6, 7) ➞ 26
- find_perimeter(20, 10) ➞ 60
- find_perimeter(2, 9) ➞ 22
"""
def find_perimeter(length, width):
    if length < 0 or width < 0:
        return "Incorrect input, cannot be less than 0"
    return (length * 2) + (width * 2)

print(find_perimeter(6, 7)) # 26
print(find_perimeter(20, 10)) # 60
print(find_perimeter(2, 9)) # 22
print(find_perimeter(-2, 9)) #Error message