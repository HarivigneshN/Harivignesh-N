vowel=["a","e","i","o","u"]
a=input()
if a in vowel:
	print ("Vowel")
elif ((a>='a' and a<='z') or (a>='A' and a<='Z')):
	print("Consonant")
else:
	print ("Invalid")
