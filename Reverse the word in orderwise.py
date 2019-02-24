a=input()
b=a[::-1].split()
c=len(b)
f=''
while(c>0):
    f=f+b[c-1]+' '
    c=c-1
print(f)
