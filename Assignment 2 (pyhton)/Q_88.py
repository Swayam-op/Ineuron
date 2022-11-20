# Write a Python program to check if a substring is present in a given string.

string = "hey there, i am swayam prakash sahoo."
sub_string = "swayam"
lis = string.split()

if sub_string in lis:
    print("substring is present in string")
else:
    print("substring is not present in string")