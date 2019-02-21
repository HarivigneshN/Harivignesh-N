s=input()
a=''
for x in s:
	if x.islower():
		a=a+x.upper()
	elif x.isupper():
		a=a+x.lower()
print(a)
