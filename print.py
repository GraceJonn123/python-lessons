#!/usr/bin/python3

import re

def main():
	print("Do you wish to store or search for a file?")
	choice = input("Type 'search' or 'store' to perform a function.\n")
	if (choice == "search"):
		search()
	elif(choice == "store"):
		store()
	else:
		raise IOError('Input either store or search')


def store():
	storage = input('What do you wish to save?\n')
	pattern = '{mytext}'
	data = "<tr><td> {} </td></tr>".format(storage)
	
	text = open('index.html', 'r+')
	for line in text.readlines():
		match = re.search(pattern, line)
		text.write(line)
		if match:
			find = line.replace(match.group(), data)
			text.write(find)
	text.truncate()
	text.close()


def search():
	searching = input('What do you wish to find?\n')
		text = open('index.html', 'r')
	for line in text:
		match = re.search(searching, line)
		if match:
			print(match.group())
	text.close()



if __name__ == "__main__":
	main()
