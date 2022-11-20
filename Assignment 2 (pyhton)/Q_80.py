# Write a Python program to check Armstrong Number.
n = input("Enter a Number\n")
#let 123 = 1pow(3)+2(pow3)+3pow(3)
leng = len(n)
n = int(n)
sum = 0;
num = n;
while(n>0):
    rem = n%10
    sum += pow(rem,leng)
    n //= 10;
print(sum)

if(num == sum):
    print(num,' is Armstrong')
else:
    print(num,' is not a Armstrong')
    