def myfun(tp):
    return tp[1]

l = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
l.sort(key = myfun)
print(l)