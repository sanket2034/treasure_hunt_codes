def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 + 1  # Logical mistake: unnecessary addition to -1.

# Main code
nums = [10, 20, 30, 40, 50]
target = 30
print("Element found at index:", linear_search(nums, target))  # Syntax mistake: missing colon in print.

# End message
print("Congratulations! You have qualified for the next round.")
