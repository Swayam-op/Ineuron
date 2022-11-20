# Write a Python program to find the n-th Fibonacci Number.
first = 0
second = 1
n = 7  #nth number
print(first,second,end=" ")
i = 2
while i<n:
    res = first + second
    print(res, end=" ")
    first = second
    second = res 
    i += 1
