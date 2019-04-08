# input : Python is a funny language
# output: language funny a is Python

s = input("Enter a string:  ")

list1 = s.split()
list2 = []
i = len(list1)-1

while i>=0:	
	list2.append(list1[i])
	i = i-1
print(' '.join(list2))