########################
# first way:

cubes = [ c**3 for c in range(11) ]
print(cubes)

#########################
# second way:

a = []
for value in range(0,11):
    a.append(value**3)
print(a)

