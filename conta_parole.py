def last():
	with open(given_file, "r") as file:
		list_of_lines = file.readlines()
		print(f"{len(list_of_lines)} {list_of_lines[-1]}")
		
last()
7776 zoom


def last():
	with open(given_file, "r") as file:
		list_of_lines = file.readlines()
		return f"{len(list_of_lines)} {list_of_lines[-1]}"


last()
7776 zoom\n

