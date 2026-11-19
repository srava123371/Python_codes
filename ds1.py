l=[101,102,103,101,104,102,105]
l1=[]
for i in l:
    if l.count(i)>1:
        if i not in l1:
            l1.append(i)
print(*l1)
