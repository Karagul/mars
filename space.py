def space(type, length):
	return " " * ({"number": 8, "username": 32, "title": 32}[type] - length)
