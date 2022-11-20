# Write a Python program to calculate the compound interest. Formula of compound 
# interest is A = P(1+ R/100)^t.
inputs = input("enter p , r ,t").split(" ")
p = int(inputs[0])
r = int(inputs[1])
t = int(inputs[2])
A = p*(pow(1 + (r/100),t))
print("A is ",A)
