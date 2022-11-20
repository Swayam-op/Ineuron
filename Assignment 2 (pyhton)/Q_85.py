# Write a Python program to find cumulative sum of a list
lis = [10,20,30,40,50]
sum = 0
new_list = []
for n in lis:
    sum += n
    new_list.append(sum)

print(new_list)