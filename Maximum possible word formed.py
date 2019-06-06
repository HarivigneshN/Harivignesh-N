a=input()
b=1
for i in range(len(a)-1):
    c=a[i]+a[i+1]
    d=int(a)
    if d<=26 and a[i]!="0":
        b+=1
if b==3:
    print(b)
else:
    print(b+(b-1)//2)
