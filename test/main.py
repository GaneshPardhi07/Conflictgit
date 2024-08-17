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

def multiply_numbers(a, b):
    return a * b

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = multiply_numbers(num1, num2)
print("The product is:", result)

print(factorial(5))  # Output: 120  

print("Hello, World!")

# Get the two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Add the two numbers
result = num1 + num2

# Print the result
print("The sum is:", result)

