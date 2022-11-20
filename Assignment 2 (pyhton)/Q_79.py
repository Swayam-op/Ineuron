#Q79. Write a Python program to check if a number is prime or not.
n = int(input("Enter a Number"))
check = False
for i in range(2,n//2+1,1):
     
     if n%i == 0:
         check = True
         break

if check :
    print(n,"is not a prime number")
else:
    print(n,"is a prime number")
    