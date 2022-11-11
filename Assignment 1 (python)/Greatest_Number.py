print("Enter 3 numbers !")
int_a = int(input())
int_b = int(input())
int_c = int(input())

if int_a > int_b and int_a > int_c:
    print(int_a, " is the greatest number.")
elif int_b > int_c:
    print(int_b, " is the greatest number.")
else:
    print(int_c, " is the greatest number.")