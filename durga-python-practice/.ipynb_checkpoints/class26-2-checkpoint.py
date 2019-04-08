# reverse string without slice and reversed() method
s = input("Enter your string: ")

n =len(s)-1

while n>-1:
	print(s[n],end='')
	n = n-1
