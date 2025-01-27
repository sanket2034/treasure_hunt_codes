def print_triangle(n):
    for i in range(1, n + 1):
        print("*" * i + 1)  # Logical mistake: adding 1 to the string.

# Main code
rows = 5
print_triangle(rows)  # Syntax mistake: missing parenthesis in function call.

# End message
print("Congratulations! You have qualified for the next round.")
