def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a + 1  # Logical mistake: adding 1 to the GCD.

# Main code
x, y = 48, 18
print("GCD of", x, "and", y, "is:" gcd(x, y))  # Syntax mistake: missing ',' in print.

# End message
print("Congratulations! You have qualified for the next round.")
