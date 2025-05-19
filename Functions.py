# def func():
#     print('hello there')
# func()

# def func(fname,lname): #parameters
#     print (fname + lname)

# func("Abdul Rehman ","Iqbal") #arguments
# func("Ali ","Iqbal")
# func("Ahmed ","Iqbal")

#arbitary arguments
# def fun(*kids):
#     print("the youngest child is:" + kids[1])
# fun("ali","hamza","ahmed")

# def func(child1,child2,child3):
#     print("the younges child is:" +child2)
# func(child1='ali',child2='ahmed',child3='hassan')

#Arbitrary Keyword Arguments, **kwargs
# def fun(**kids):
#     print("his first name is:" + kids['lname'])
# fun(fname='Ali', lname='ahmed')

# def func(food):
#     for x in food:
#         print(x)
# fruit=['apple','banana','cherry']
# func(fruit)

# def func(x):
#     return 5 * x
# print(func(3))
# print(func(10))

# def func # if only postional argument needed ( x,/),  # if only keyword argument needed (*,x):
#     print (x)
# func(10)
# func(20)

# combine postional and keyword argument
# def func(x,y,/,*,a,b):
#     print(x+y+a+b)
# func(10,20,a=30,b=10)


# # Nonlocal keyword in scope of nested function
# def func1():
#     x='AR'
#     def func2():
#         nonlocal x
#         x="Ali"
#     func2()
#     return x
# print(func1())