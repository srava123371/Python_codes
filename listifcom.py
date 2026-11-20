marks = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}
print([n for n in marks.values() if n%2==0])
print(tuple(n for n in marks.values() if n%2==0))
print({n for n in marks.values() if n%2==0})
print({n: n**2 for n in marks.values() if n%2==0})
