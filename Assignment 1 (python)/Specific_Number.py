numbers = [12, 75, 150, 180, 145, 525, 50]

for n in numbers:
    if n%5 == 0 and n <= 150 :
        print(n , end=" ")
    if n > 500:
        break 