# Write a Python program to interchange the first and last element in a list.

lis = [1,2,3,4,5]
first_element = lis[0]
lis[0] = lis[len(lis)-1]
lis[len(lis)-1] = first_element
print(lis)