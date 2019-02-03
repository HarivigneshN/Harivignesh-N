a=int(input())
if (a % 4) == 0:
   if (a % 10) == 0:
       if (a % 40) == 0:
           print("yes")
       else:
           print("no")
   else:
       print("yes")
else:
   print("no")
	
