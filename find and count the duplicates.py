a=input().split()
b=[x for n, x in enumerate(a) if x not in a[:n]]
print(b)
c=[x for n, x in enumerate(a) if x in a[:n]]
print(c)
