#variables to store data in system 
student_count = 1000
rating = float(4.99)
is_published = True
course_name ="Python Programming"

#unpack a collection 
fruits = ["apple","banana","cherry"]
x,y,z = fruits
#print(x,y,z)

#global variables
x = "awesome"
def func():
#if you want to change the value of global variable inside a function, you can use global keyword
    global x
    x="fantastic"
func()
print("Python is "+ x)