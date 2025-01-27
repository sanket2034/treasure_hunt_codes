def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count  # Logical mistake: didn't handle non-alphabetic characters.

# Main code
text = "This is a test"
print("Vowel Count:" count_vowels(text))  # Syntax mistake: missing '+' operator in print.

# End message
print("Congratulations! You have qualified for the next round.")
