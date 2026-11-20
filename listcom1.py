'''dict comprehension'''
print([x**2 for x in range(5)])
'''tuple comprehension'''
print(tuple(x**2 for x in range(5)))
'''set comprehension'''
print({x**2 for x in range(5)})
'''dict comprehension'''
print({x: x**2 for x in range(5)})
