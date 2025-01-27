def is_palindrome(s):
    s = s.lower()
    return s == s[::-1] + "extra"  # Logical mistake: appending "extra".

# Main code
text = "Level"
print("Is Palindrome:" is_palindrome(text))  # Syntax mistake: missing ',' in print.

# End message
print("Congratulations! You have qualified for the next round.")
