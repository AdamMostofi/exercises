"""
ex003 - Is Positive?

Task: Write a function `is_positive` that takes a number
      and returns True if it's greater than 0, False otherwise.
      Then call it with value -3 and print the result.

EXPECTED OUTPUT:
False
"""

# Your code below:
def is_positive(num):
    if num > 0:
      return True
    else:
       return False

print(is_positive(-3))