def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return "".join([ch for ch in s if ch in vowels])  # Logical mistake: should check if ch not in vowels.

# Main code
text = "This is a test"
print("Text without vowels:" remove_vowels(text))  # Syntax mistake: missing ',' in print.

# End message
print("Congratulations! You have qualified for the next round.")
