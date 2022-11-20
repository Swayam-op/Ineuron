for i in range(4,-1,-1):
    for j in range(5):
        if j >= i:
            print("* ",end="")
        else:
            print(" ",end="")
    print()
