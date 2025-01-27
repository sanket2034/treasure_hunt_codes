def team9():
    nums = [1, 2, 3, 4, 5]
    print(nums(2))  # Syntax Error: Incorrect indexing syntax, should use []
    total = sum(nums) - nums[-1]  # Logical Error: Incorrect total calculation
    print(f"Total: {total}")
    print("You qualify for the next round!")

team9()
