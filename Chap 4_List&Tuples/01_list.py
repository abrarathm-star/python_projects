# LIST INDEXING

l1= ["Abrar", 25, 36, 9.8, False,True, "Urooj", "Uni", "Job"]


print(l1[8])            # output ---> Job
print(type(l1[8]))      #outut --->


print(l1[1])            # output ---> 25
print(type(l1[1]))      #outut ---> <class 'int'>


print(l1[7])            #outut ---> Uni
print(type(l1[7]))      #outut ---> <class 'str'>

print(l1[0])            #output ---> Abrar
print(type(l1[0]))      # output ---> <class 'str'>



# Replacing an index in a List:

l1[7]="khan"            #this will change index[7] to khan.


print(l1)               # output ---> ['Abrar', 25, 36, 9.8, False, True, 'Urooj', 'khan', 'Job']  # Index [7] was uni ---> becomes khan
print(type(l1))         # output ---> <class 'list'>

l1[0]= 1                #"Abrar" ---> 1
print(l1)               #output ---> [1, 25, 36, 9.8, False, True, 'Urooj', 'khan', 'Job']

"""List are mutable (changeable)"""