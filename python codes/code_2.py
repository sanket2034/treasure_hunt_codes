def team2():
    lst = [1, 2, 3, 4]
    for i in range(5):  # Logical Error: Out-of-range loop
        print(lst[i])  # Will cause IndexError
    print("You qualify for the next round!")  # Won't execute due to the error

team2()
