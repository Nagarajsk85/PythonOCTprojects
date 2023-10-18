# Input list of numbers
numbers = [12, -7, 5, 64, -14]
numbers1 = [12, 14, -95, 3]
# Iterate through the first list and print positive numbers
print("Positive numbers in the first list:")
for num in numbers:
    if num > 0:
        print(num)
# Iterate through the second list and print positive numbers 
print("\nPositive numbers in the second list:")
for num in numbers1:
    if num > 0:
        print([num])
