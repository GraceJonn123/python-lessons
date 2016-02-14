def main():
	a, b = 79, 78#these are variables(assignment)
	if a > b:#this is a conditional
		#this colon means there will be a line of code indented under it.
		print("a is greater than b")
	elif a < b:
		print("a is less than b")
	else:
		print("a is equal to b")

if __name__ == "__main__": main()


#There is a shorter way
#def main():
#	if a, b = 5, 8
#	s = "less than" if a < b else "not less than"
#