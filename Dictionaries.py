# # ar={
# #     "Name": "Abdulrehman iqbal",
# #     "Profession":"IT Engineer",
# #     "Age":22,
# #     "Country":["Pakistan", "USA", "UK"]

# #     }
# # print(ar)

# #constructor
# # ar=dict(name="abdulrehman",age=22,professiona="IT Engingeer",country=`"Pakistan")
# # print(ar)

# # ar={
# #     "name":"abdulrehman",
# #     "age":22,
# #     "profession":"IT Engineer",
# #     "country":"Pakistan",

# # }
# # x=ar.get("name")
# # x=ar.keys()
# # print(x)
# # ar["skills"]=["Python", "Java", "C++"]
# # print(x)

# # x=ar.values()
# # print(x)
# # ar['country']="USA"
# #add new item
# # ar["height"]=5.9
# # print(x)

# #display all items in list of tuples
# # x=ar.items()
# # print(x)

# # ar={
# #     "name":"abdulrehman",
# #     "age":22,
# #     "profession":"IT Engineer",
# #     "country":"Pakistan",

# # }
# # if "name" in ar:
# #     print("yes")
# # else:
# #     print("no")

# # ar={
# #     "name":"abdulrehman",
# #     "age":22,
# #     "profession":"IT Engineer",
# #     "country":"Pakistan",

# # }
# # ar.update({"name":"abdulrehman iqbal"})
# # ar.pop("age")
# # ar.popitem()
# # del ar["profession"]
# # ar.clear()
# # print(ar)

# # ar={
# #     "name":"abdulrehman",
# #     "age":22,
# #     "profession":"IT Engineer",
# #     "country":"Pakistan",

# # }
# #print only keys
# # for x in ar:
# #     print(x)

# #pritn only values
# # for x in ar.values():
#     # # print(x)

# #print both keys and values
# # for x,y in ar.items():
# #     print(x,y)

# #copy dictionary
# # thisdict=ar.copy()
# # thisdict=dict(ar)
# # print(thisdict)


# #nested dictionary
# arfamily={
#     "bhai":{
#         "name":"naseeb",
#         "age":32,
#         "profession":"accountant",
#     },
#     "Zaid":{
#         "name":"zaid",
#         "age":28,
#         "profession":"Fastiya Owner",
#     },
#     "kiran":{
#         "name":"kiran",
#         "age":22,
#         "profession":"student",
#     }
# }
# # print(arfamily)
# # print(arfamily.values())
# # print(arfamily.keys())
# # print(arfamily["bhai"].keys())
# # print(arfamily["bhai"].values())


#create 3 dictonaries and add in a single dictrionary
# ar1={
#     "name":"abdulrehman",
#     "age":22,
#     "profession":"IT Engineer",
#     "country":"Pakistan",
# },
# ar2={
#     "goals":"to become a software engineer",
#     "skills":["Python", "Java", "C++"],
# },
# ar3={
#     "hobbies":["reading", "writing", "coding"],
#     "languages":["English", "Urdu", "Punjabi"],
# }

# ardict={
#     "ar1":ar1,
#     "ar2":ar2,
#     "ar3":ar3,
#     }
# print(ardict)
# print(ardict["ar1"])


#loops in nested dictionary
# artribe={
#     "bhai":{
#         "name":"naseeb",
#         "age":32,
#         "profession":"accountant"
#     },
#     "zaid":{
#         "name":"zaid",
#         "age":28,
#         "profession":"Fastiya Owner"
#     },
# "sana":{
#         "name":"sana",
#         "age":31,
#         "profession":"student"
#     },
# }

# for x, obj in artribe.items():
#     print(x)
#     for y in obj:
#         print(y + ":",obj[y])