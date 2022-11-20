# Write a Python program to find words which are greater than given length k.

words = ["swayam" , "bimal", "rock" , "audi", "speaker" , "cat" , "aeroplane"]
k = 5

for word in words :
    if len(word) > 5:
        print(word, end=" ")