#python generators

#difference between generator and list is that generator does not store values in memory and returns one value at a time whereas list runs the results all at once.

# gen_exp=(x*2 for x in range(10))
# print(next(gen_exp))
# print(next(gen_exp))
# print(next(gen_exp))

# gen=(x*2 for x in range(10))
# for value in gen:
#     print(value)


# even_gen=(x for x in range(20) if x %2==0)    
# print(set(even_gen))