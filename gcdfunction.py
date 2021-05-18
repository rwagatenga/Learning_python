def gcdfunc(x, y):
    min = x if x < y else y
    largestFactor = 1
    for i in range(1, min + 1):
        if x % i == 0 and y % i == 0:
            largestFactor = i
    return largestFactor


print(gcdfunc(36, 48))