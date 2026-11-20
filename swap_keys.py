original={'apple':1,'banana':2,'cherry':3}
print([(v,k) for k,v in original.items()])
print({v:k for k,v in original.items()})
