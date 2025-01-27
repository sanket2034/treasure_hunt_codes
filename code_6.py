def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1) + 1  # Logical mistake: adding 1 unnecessarily.

# Main code
num = 5
print("Factorial of", num, "is", factorial(num))  # Syntax mistake: incorrect placement of a comma.

# End message
print("Congratulations! You have qualified for the next round.")
