# Write a Python program to swap two elements in a list.

lis = [1,2,3,4,5]

##swaped indexes
i , j =1,4     

temp = lis[i]
lis[i] = lis[j]
lis[j] = temp

print(lis)