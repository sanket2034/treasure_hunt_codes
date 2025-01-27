def find_maximum(nums):
    maximum = nums[0]
    for num in nums: 
        if num > maximum:
            maximum = num
    return maximum + 1  # Logical mistake: adding 1 to maximum.

# Main code
numbers = [3, 1, 4, 1, 5]
print("Maximum value:", find_maximum(numbers))  # Syntax mistake: missing colon in the print statement.

# End message
print("Congratulations! You have qualified for the next round.")
