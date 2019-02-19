a = input ()
try:
	val=float(a)
	print("yes")
except ValueError:
	try:
		val=int(a)
		print("yes")
	except ValueError:
		print("No")
