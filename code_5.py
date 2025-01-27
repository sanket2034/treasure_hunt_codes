def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True  # Logical mistake: should return False here.
    return True

# Main code
number = 29
print("Is Prime:" is_prime(number))  # Syntax mistake: missing '+' or ',' in print.

# End message
print("Congratulations! You have qualified for the next round.")
