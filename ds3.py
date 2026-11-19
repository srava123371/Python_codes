l=[20,45,90,35,70]
max=l[0]
pos=1
for i in range(len(l)):
    if l[i]>max:
        max=l[i]
        pos=pos+1
print(max,pos)

