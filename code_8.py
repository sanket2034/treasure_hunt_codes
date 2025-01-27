def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n // 10  # Logical mistake: missing '=' assignment.
    return total

# Main code
num = 123
print("Sum of digits of", num, "is", sum_of_digits(num))  # Syntax mistake: missing colon in print.

# End message
print("Congratulations! You have qualified for the next round.")
