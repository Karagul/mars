import sys
from evaluate import *
from output import *

def main(passwords):
	output(["Number", "Username", "Title", "Password"])
	number = 0
	while True:
		evaluate(number, passwords)
		number += 1

if __name__ == "__main__":
	try:
		file = open("passwords.txt", "r")
		passwords = file.read().split("\n")[:-1]
		main(passwords)
	except KeyboardInterrupt: sys.stdout.write("\nInterrupted.\n\n")
	except Exception as error:
		sys.stdout.write("An error occurred: " + str(error) + "\n")
	finally: file.close()
