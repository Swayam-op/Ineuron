ch = 'A'
for i in range(5):
    for j in range(i+1):
        print(ch,end=" ")
    ch  = chr(ord(ch)+1)
    print()