b = input ()
try:
	v=float(b)
	print("yes")
except ValueError:
	try:
		v=int(b)
		print("yes")
	except ValueError:
		print("no")
