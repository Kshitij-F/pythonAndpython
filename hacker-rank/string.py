string =input("Enter your string: ")
subs_string = input("Enter a subtring to find: ")

pos = -1

while True:
	pos = string.find(subs_string,pos+1,len(string))
	if pos == -1:
		break
	print("substring found at {}".format(pos))
	



# print(s.find(subs))

