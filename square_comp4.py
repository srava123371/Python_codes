print([x    **2 for x in range(10) if x%2==0])
print(tuple(x**2 for x in range(10) if x%2==0))
print({x**2 for x in range(10) if x%2==0})
print({x: x**2 for x in range(10) if x%2==0})