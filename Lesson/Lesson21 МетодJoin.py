l = list(range(1, 10))
l2 = list('hello')

print(l)

s = '-'.join(map(str, l))

s2 = '%'.join(l2)
print(s, s2, sep=("\n"))