import sys

def output(entry):
	number = 0
	for item in entry:
		sys.stdout.write(str(item) + \
			" " * ([8, 32, 32, 8][number] - len(str(item))))
		number += 1
	sys.stdout.write("\n")
