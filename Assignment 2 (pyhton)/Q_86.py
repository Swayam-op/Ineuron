# Write a Python program to check if a string is palindrome or not.
string = "ababa"
rev_string = ""
for i in range(len(string)-1,-1,-1):
    rev_string += string[i]
    
if string == rev_string:
    print("string is palindrome.")
else:
    print("string is not palindrome")