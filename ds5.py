l=[100,250,300,150,400]
b=550
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==b:
            print(l[i],l[j])
            break
    else:
        continue
    break
            

