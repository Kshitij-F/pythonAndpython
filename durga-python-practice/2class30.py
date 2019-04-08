l1 = [1,2,3,4,5,6,7]

x = input("Enter the element to remove: ")

if x in l1:
	l1.remove(x)
	print('{} removed from the list'.format(x))
	print(l1)
else:
	print("Specified element is not in the list")