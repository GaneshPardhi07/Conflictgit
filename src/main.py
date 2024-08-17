## Main branch changes code 

## prime number function inpython

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) +  1):
        if num % i == 0:
            return False
    return True

# Test the function
print(is_prime(11))  # Output: True
print(is_prime(35))  # Output: False

def power(base, exponent):
    return base ** exponent

# Test the function
print(power(2, 3))  # Output: 8
print(power(3, 4))  # Output: 81