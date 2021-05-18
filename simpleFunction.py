# Definition of the prompt function
def prompts(n):
    value = int(input("Please enter integer #"))
    return value
print("This program adds together two integers.")
value1 = prompts(1)
# Call the function
value2 = prompts(2)
# Call the function again
sum = value1 + value2
print(value1, "+", value2, "=", sum)