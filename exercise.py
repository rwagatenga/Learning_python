n = eval(input("Enter a number: "))
if n < 1:
    print(" ", end="")
else:
    for row in range(1, n):
        for col in range(1, n + 1):
            print("*", end="")
        print()