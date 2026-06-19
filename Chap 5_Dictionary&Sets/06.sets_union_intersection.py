a={2,4,6,8,10,12,14,16,18}
b={3,6,9,12,15,18,21,24}

# union

print(a.union(b))

# intersection

print(a.intersection(b))

# difference

print(a-b)

"""note : (a-b) is not eqaul to (b-a)"""

# Symmetric difference (Delta)

print(a^b)