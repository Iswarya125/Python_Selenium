from selenium import webdriver

#multiple declarations in single line
a, b, c = 3, 4, 5

#del function - to delete
list1 = [1,2,3,4,5]
del list1[2]
print(list1)
tuple1 =(1,2,3,4)
del tuple1

a = 1
while a < 5:
    print(a)
    a+=1
else:
    print('inside else')
    print(a)

class vehicle:
    number = 10
    def __init__(self,a,b):
        print("inside constructor")
    def __del__(self):
        print("inside destructor")
    def printer(self):
        print(vehicle.number)
        print(self.number)

class car(vehicle):
    def __init__(self):
        #call base class constructor explicitly if it is not default one,
        #notice self is passed
        vehicle.__init__(self,2,3)
    def printer1(self):
        print(vehicle.number)

v = vehicle(1,2)
v.printer()
print(type(v))

c = car()
c.printer1()



try:
    i = 10/0
except:
    print('excepted')

try:
    i = 10/0
except Exception as e:
    print(e)

try:
    raise Exception('Hello exception')
except Exception as e:
    print(e)

a = 2
try:
    assert (a != 2)
except:
    print("assertion failure")
finally:
    print("resource or cookies clean up")

try:
    assert (a == 2)
except:
    print("assertion failure")
finally:
    print("resource or cookies clean up")

#file methods: read -> reads the complete file -> If argument is passed that many characters are read
#              readline -> To read line by line
#              readlines -> similar to read, but stores the result into a list (i.e each line is stored as single element in the list)

#               write and writelines -> both prints to same line

#reversed -> to reverse the list
list2=[0,1,2,3,4,5]
list3=['1','2','3']
print(list2)
for element in reversed(list2):
    print(element)


with open("new.txt", 'w') as writer:
    writer.writelines("hello")
    writer.writelines("hai")
    writer.write("hello")
    writer.write("hai")
#    writer.write(list2) - error
#    writer.writelines(list2) - error  as arguments must be str


