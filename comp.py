
l = [1, 3, 5]
p = [n*2 for n in l]
print(p)

# the above is the same as the below - this is a list conprenhension

p = []
for n in l:
    p.append(n * 2)
print(p)


# chanllenge

print([ i*2 for i in range(7)])

