# Write a Python program to find the factorial of a given number.
n = int(input("Enter a number \n"))
fac = 1
for i in range(1,n+1):
    fac *= i

print(f"Factorial of {n} is {fac}")

