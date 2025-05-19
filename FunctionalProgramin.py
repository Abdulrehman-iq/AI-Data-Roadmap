# # #lambda is used for creating small anonymous functions

# # #lambda arguments:expression (rule)
# # addd=lambda x,y:x+y
# # result=addd(5,10)
# # print(result)

# square=lambda x: x*2
# print(square(5))

# cube=lambda x: x*x*x
# print(cube(5))

# avg=lambda x,y,z:(x+y+z)/3
# print(avg(5,10,20)  )

#similar function and lambda example below
# def func(x,y):
#     return x+y
# print(func(5,10))

# add=lambda x,y:x+y
# print(add(5,10))

#Maps
# map(function,iterable )
#map is used to apply function to all items present in iterable(i-e list, tuple, etc) and returns new iterable

# def square(x):
#     return x*x

# l=[1,2,3,4,5]
# newl=set(map(square,l))
# print(newl)

#map using lambda
# nums=[1,2,3,4,5]
# newl=list(map(lambda x:x*x*x,nums))
# print(newl)

#filter
#filter(function,iterable )


# nums=[1,2,3,4,5]

# def filter_func(x):
#     return x>2

# newl=tuple(filter(filter_func,nums))
# print(newl)

#filter using lambda
# nums=[13,22,33,42,50]
# newl=set(filter(lambda x:x%2==0,nums))
# print(newl)

#reduce
#reduce(function,iterable)
#reduce is used to apply function to the iterable and returns a single value

# from functools import reduce

# # def sum(x,y):
# #     return x+y

# # nums=[1,2,3,4,5]

# # newl= reduce(sum,nums)
# # print(newl)

#reduce using lambda
nums=[1,2,3,4,5]
newl=reduce(lambda x,y:x-y,nums)
print(newl)



