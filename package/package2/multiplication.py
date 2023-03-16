def mult(*args):
	total = args[0]
	for arg in args[1:]:
		total *= arg
	return total