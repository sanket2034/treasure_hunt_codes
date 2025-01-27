def team5():
    x = 5
    for i in range(x):  # Logical Error: Should iterate only 4 times
        print(x + i)
    print(f"Sum of i and x: {sum(x + i for i in range(x)})  # Syntax Error: Missing closing parenthesis
    print("You qualify for the next round!")

team5()
