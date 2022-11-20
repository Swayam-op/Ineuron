tp1 = (7,2)
tp2 = (7,8)

lis = [(x,y) for x in tp1 for y in tp2]
lis2 = [(x,y) for x in tp2 for y in tp1]
lis.extend(lis2)
print(lis)