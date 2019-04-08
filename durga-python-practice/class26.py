# To check the type of an element in the string

# INPUT: Enter anything from keyboard:
# OUTPUT: output will state if it is a alpahanumeric, alphabet, lowercase, uppercase, digit, space only, non space special character

s = input("Enter anything character: ")

if s.isalnum():
	print("alpahanumeric")
	if s.isalpha():
		print("alphabet")
		if s.islower():
			print("lowercase")
		else:
			print("uppercase")
	else:
		print('digit')
elif s.isspace():
	print("space only")
else:
	print("non space special character")

