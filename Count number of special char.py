a = input ()
b=0
for i in a:
	if i.isalpha() or i.isnumeric():
		b=b+1
print(len(a)-b)		
		
