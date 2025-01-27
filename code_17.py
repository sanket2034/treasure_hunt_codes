def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = sum([int(digit)**power for digit in num_str])
    return total == n + 1  # Logical mistake: adding 1 unnecessarily.

# Main code
num = 153
print("Is Armstrong:" is_armstrong(num))  # Syntax mistake: missing ',' in print.

# End message
print("Congratulations! You have qualified for the next round.")
