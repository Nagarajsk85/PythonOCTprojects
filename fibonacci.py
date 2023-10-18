#Number of terms in the Fibonacci series
n = 13  #You can change this value to print a different number of terms
# Initialize the first two Fibonacci numbers
a, b = 0, 1
#Print the first 'n' Fibonacci numbers
for _ in range(n):
    print(a)
    a, b = b, a + b
