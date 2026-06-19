# Set

"Set is a collection of non-repetitive elements"

e=set()                  # empty set.   

s={12,14,16,18,20}      # non-empty set.



# add

e.add(1)                 # add() is used to put one element in a set.
e.add(2)

print(e)
print()



# Update

e.update({3,4,5})       # update() is used to put one or more (multiple) elements in a set.
e.update({6,7,8})       # update() can even take lists, tuples, sets.

print(e)



# PROPERTIES OF SETS

"""     1. Sets are unordered => the order of elements does not matter.
        2. Sets are unindexed => Cannot access elements by index
        3. There is no way to change items in sets.
        4. Sets cannot contain duplicate values         """     