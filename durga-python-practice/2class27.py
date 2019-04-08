my_list = ['A','B','C','D']
x = len(my_list)

i = 0
while i< len(my_list):
    print("positive index : ",i,"negative index: ",i-x)
    i = i+1
    
    
def f1():
    print("This is function")

class Student:
    def info(self):
        print("This is method")

s=Student()
s.info()