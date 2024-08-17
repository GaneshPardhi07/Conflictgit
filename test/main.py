## Test code for palidrom number

def is_palindrome(s):
    return s == s[::-1]

# Test the function
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
print(factorial(5))  # Output: 120