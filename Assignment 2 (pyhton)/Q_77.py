# Write a Python program to calculate the simple interest. Formula to calculate 
# simple interest is SI = (P*R*T)/100
inputs = input("enter P R T").split(" ")
P = int(inputs[0])
R = int(inputs[1])
T = int(inputs[2])

SI = (P*R*T)/100
print(f"Simple Interest is {SI}")