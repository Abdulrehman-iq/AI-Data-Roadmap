# thisset={"apple",1,True,False,0,2}
# print(len(thisset))

# thisset=(("apple",1,"True" ,"False",0,2))
# print('applew' not in thisset)


#add data in set from another set
# thisset = {"apple", "banana", "cherry"}
# myset = {"kiwi", "orange"}
# lastset=('mango',)  #any iterable(data structure type can be used to add data in set)
# listset=['grapes','peach']
# thisset.update(myset,lastset,listset)
# print (thisset)


# thisset = {"apple", "banana", "cherry"}
# # thiset.discard("bansana")
# # x=thiset.pop()
# thisset.clear()# print(x)
# print(thisset)

#join sets in python
#union
# set1 = {"a", "b" , "c"}
# set2={1,2,3}
# # set3=set1.union(set2)
# set3=set1|set2
# print(set3)

#join multiple sets
# set1 = {"a", "b" , "c"}
# set2={1,2,3}
# set3={4,5,6}
# set4={'zaid','ali'}
# set5=set2.union(set1,set3,set4)
# print(set5)

# x={"apple","banana","cherry"}
# y=["google","microsoft","apple"]
# z=x.union(y)
# print(z)

#intersection
# set1={"apple","banana","cherry"}
# set2={"google","microsoft","apple"}

# # set3=set2.intersection(set1)
# set3=set1&set2
# print(set3)

#intersection_update

# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set1.intersection_update(set2)
# print(set1)

#difference
# set1 = {"abdulrehman", "banana", "cherry"}
# set2 = {"google", "microsoft", "abdulrehman"}
# # set3=set1.difference(set2)
# set3=set1-set2
# print(set3)

#difference_update
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1-=set2
# set1.difference_update(set2)
# print(set1) 

# #symmetric_difference
# set1={"apple","banana","cherry"}
# set2={"google","microsoft","apple"}
# # set3=set1.symmetric_difference(set2)
# # set3=set1^set2
# set1.symmetric_difference_update(set2)
# print(set1)
