def reverse_string(s):
    result = s[::-1]  # Logical mistake: forgot to remove whitespaces before reversing.
    return result

# Main code
string = "hello world"
print("Reversed String:", reverse_string(string))  # Syntax mistake: missing a parenthesis.

# End message
print("Congratulations! You have qualified for the next round.")
