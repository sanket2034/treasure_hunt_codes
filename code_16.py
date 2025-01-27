def binary_search(arr, target):
    left, right = 0, len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 - 1  # Logical mistake: unnecessary subtraction from -1.

# Main code
nums = [10, 20, 30, 40, 50]
target = 40
print("Element found at index:" binary_search(nums, target))  # Syntax mistake: missing ',' in print.

# End message
print("Congratulations! You have qualified for the next round.")
