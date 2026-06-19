a=(1,2,"abrar", 34.55,6,2,1,2,3,2,5,2)
b=((9,6,34.55,6,19,1,44,3,90,12,10))

# 1.count()

print(a.count("abrar"))
print(a.count(2))



# 2. index()

print(a.index(2))



# 3. len()     ---> length of a tuple
print(len(a))



# 4. max()

print(max(b))



# 5. min()

print(min(b))



# 6. sum()

print(sum(b))



# 7. slicing:

c=a[2:5]
d=b[0:5]
print(c)        # output ---> ('abrar', 34.55, 6)
print(d)        #output ---> (9, 6, 34.55, 6, 19)


# 8. unpacking:         
'''will learn later'''