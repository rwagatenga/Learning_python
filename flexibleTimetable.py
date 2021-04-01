MAX = 18
print(end="       ")

for column in range(1, MAX + 1):
    print(" %2i " % column)
print()

print(end="  +")

for column in range(1, MAX + 1):
    print(end="----")
print()

for row in range(1, MAX + 1):
    print(end="%2i  | " % row)
    for col in range(1, MAX + 1):
        product = row * col
        print(end="%3i" % product)
    print()