# String is a data type in python. String is a sequence of characters enclosed in quotes. 
# We can primarily write a string in these three ways.

a='Abrar'            #single quoted string.
b="Abrar"            # Double quoted String.
c="""Abrar"""        # Triple quoted String.


# STRING SLICING:

name="abrar"

name_short = name[0:3]                  # start from index 0 all the way to 3(excluding 3)
print(name_short)
print()

person_1_p1 = "Hammad"
p1=person_1_p1[2:5]
print(p1)


print(name[:4])                         #[:4] ---> [0:4]

print(name[2:])                         #[2:] ---> [2:till the end]