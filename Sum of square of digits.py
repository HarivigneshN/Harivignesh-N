a = int(input())
s = 0
while a > 0:
    d = a%10
    a = a//10
    s = d**2+s
print(s)
