# Take input from users (always stored as STRING by default)

a=input("first number: ")       # first input (as a STRING)
b=input("second number: ")      # second input (as a STRING)


# Print Values of 'a' and 'b' (just to check what user has entered)

print("number a is: ", a)
print("number b is: ", b)


# add a and b
print("sum is: ", a+b)          # but since 'a' and 'b' are STRINGS, this will join the numbers instead of adding them i.e. a+b = 23 not 5.
print()


# now 