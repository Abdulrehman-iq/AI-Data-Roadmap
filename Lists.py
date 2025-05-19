{# #Arrays
# cars=["bmw","audi","toyota","subaru"]
# # x=cars[3]
# # cars[2]="honda"
# # print(cars)

# # cars=["bmw","audi","toyota","subaru"]
# # x=len(cars)
# # print(x)

# cars.append("AR Honda")
# cars.pop(2)
# cars.remove("audi")
# print(cars)
}

#################################
#Lists

{#mylist = ["apple", "banana", "cherry","orange","kiwi","melon","mango"]
    # print(mylist)
}

{#list constructor
# thislist=list(("apple", "banana", "cherry","orange"))
# print(thislist)
    }
# if "apple" in mylist:
#     print("Yes, 'apple' is in the fruits list")

{#negative indexing
# print(mylist[-5:-2])
}

# thislist = ["apple", "banana", "cherry"]
# # thislist.insert(2, "watermelon")
# # print(thislist)

{
#Extend list from another list
# mylist=['abdulrehman','zain','ali','ahmed']
# lastlist=['zain','usman','umer']
# mylist.extend(lastlist)
# #del mylist[0]
# # mylist.pop(4)
# #mylist.clear()
# print(mylist)
}

# number = list(range(1,10))
# print(number)

{
#loops in list
#thislist=['apple','banana','cherry']
# for x in range(len(thislist)):
#     print(thislist[x])

# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i+=1
}

{
#list comprehension
# [print( x) for x in thislist]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[]
# for x in fruits:
#     if 'a' in x:
#         newlist.append(x)
# print(newlist)

# secondlist=[x for x in fruits if 'a' in x]
# print(secondlist)

# newlist=[x for x in range(10) if x%2==0] 
# newlist=[x.upper for x in fruits]

# newlist=[x if x!='banana' else 'orange' for x in fruits]


# print(newlist)
}

{
#list sort  
# thislist=[1,2,3,4,5,6,7,8,9]
# thislist.sort(reverse=True)
# print(thislist)

# def func(n):
#     return abs(n-50)

# thislist=[100,50,65,82,23]
# thislist.sort(key=func)
# print(thislist)
}

#  copy list
# thislist = ["apple", "banana", "cherry"]
# # mylist=thislist.copy()
# mylist=list(thislist)
# print(mylist)

