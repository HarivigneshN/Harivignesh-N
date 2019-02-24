a=input()
a=a.casefold()
b = reversed(a)
if list(a) == list(b):
	print("YES")
else:
	print("NO")
