def permute(LIST):
    length=len(LIST)
    if length <= 1:
        yield LIST
    else:
        for n in range(0,length):
             for end in permute( LIST[:n] + LIST[n+1:] ):
                 yield [ LIST[n] ] + end

a=int(input())
b=[]
for i in range(0,a):
	b.append(i)
	for x in permute(b):
		print (x)
