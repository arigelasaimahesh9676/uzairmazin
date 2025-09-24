def factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120.
    """
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage:
number = 5
print(f"The factorial of {number} is: {factorial(number)}")

number = 0
print(f"The factorial of {number} is: {factorial(number)}")
