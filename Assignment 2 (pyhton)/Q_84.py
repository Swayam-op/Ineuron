# Write a Python program to find N largest element from a list.
lis = [2,5,1,6,12,7,3]
N = 3

lis.sort()
print(N,"largest element from a list is : ", lis[len(lis)-N])