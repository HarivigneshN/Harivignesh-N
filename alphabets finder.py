a=input()
if((a>='a' and a<='z') or (a>='A' and a<='Z')):
	print ("Given is an Alphabet")
else:
	print("Given is not an Alphabet ")
	
#####Another method#####

if a.isalpha() == True:
   print("All characters are alphabets")
else:
    print("All characters are not alphabets.")
