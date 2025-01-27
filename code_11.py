def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a = b
        b = a + b  # Logical mistake: should be b = a + b, a = b.

# Main code
print("Fibonacci Series:", list(fibonacci(5)))  # Syntax mistake: incorrect function call brackets.

# End message
print("Congratulations! You have qualified for the next round.")
