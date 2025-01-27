def find_smallest(nums):
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest + 1  # Logical mistake: adding 1 to the smallest element.

# Main code
numbers = [3, 1, 4, 1, 5]
print("Smallest number is:", find_smallest(numbers))  # Syntax mistake: missing colon in print.

# End message
print("Congratulations! You have qualified for the next round.")
