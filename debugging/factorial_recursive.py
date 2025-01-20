#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function to calculate the factorial of a given number n using recursion.

    Parameters:
        n (int): The number for which the factorial will be computed. It must be a non-negative integer.

    Returns:
        int: The factorial of the input number n. If n is 0, returns 1 (as 0! = 1).
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive case: n! = n * (n-1)!

# Convert the command line argument to an integer and calculate the factorial
f = factorial(int(sys.argv[1]))

# Print the result of the factorial calculation
print(f)
