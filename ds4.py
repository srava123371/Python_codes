l=[5,3,0,4,6,2,0,8]
c=0
for i in range(len(l)-1):
    if l[i]>0 and l[i+1]>0:
        c+=1
print(c)

