for first in "ABC":
    for second in "ABC":
        if second != first:
            for third in "ABC":
                if third != first and third != second:
                    print(first + second + third)

entry = 0
sum = 0
print("Enter numbers to sum, note: negative number will end the list")

while True:
    entry = eval(input())
    if entry < 0:
        break
    sum += entry
print("Sum = ", sum)
