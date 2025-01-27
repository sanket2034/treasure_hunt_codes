def find_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total * 2  # Logical mistake: multiplying by 2 unnecessarily.

# Main code
numbers = [1, 2, 3, 4]
print("Sum of list is:", find_sum(numbers))  # Syntax mistake: missing colon in print.

# End message
print("Congratulations! You have qualified for the next round.")
