a=input()
a=a.casefold()
b=a[::-1]
if a==b:
	c=b[1:]
	print(c[::-1])
else:
	print(a)
