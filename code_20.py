def transpose(matrix):
    return [[row[col] for row in matrix] for col in range(len(matrix))]  # Logical mistake: swapping row and col incorrectly.

# Main code
matrix = [[1, 2], [3, 4]]
print("Transposed Matrix:", transpose(matrix))  # Syntax mistake: missing colon in print.

# End message
print("Congratulations! You have qualified for the next round.")
