# #  1. LENGTH OF A STRING:

# name="MuhammadAbrar"
# print(len(name))                        #len() funtion ---> shows length of a string. # Output is 13.
# print()

# sister="urooj"
# print(len(sister))
# print()

# uni="hochschuele_Muenchen"
# print(len(uni))
# print()



# #   2. endswith() ---> END OF A STRING:

# print(name.endswith("rar"))             # (write variable).endswith() function ---> shows true or false. output is true
# print()



# #   3. startswith() ---> Start of a String:
# uni="hochschuele_Muenchen"              #(write variable).endswith() function ---> shows true or false. output is true
# start=uni.startswith("ho")
# print(start)
# print()

# name="MuhammadAbrar"
# start1=name.startswith("Ma")
# print(start1)
# print()



#   4. count() ---> STRING COUNT:

# count=name.count("a")                   #   (write variable).count() function ---> shows how many 'a' are in the string.
# print(count)
# print()
                 
uni="hochschuele_Muenchen"
print(uni.count("u"))
print()

sentence="I am from karachi pakistan"
number_of_a=sentence.count("a")
print(number_of_a)
print()



# #   5. capitalize() (Capitalize The first character):

# name="MuhammadAbrar"
# Capitalized_string=name.capitalize()
# print(Capitalized_string)                   #output:Muhammadabrar
# print()

# uni="hochschuele_Muenchen"
# make_cap=uni.capitalize()
# print(make_cap)
# print()



# #   6. find() ---> FIND A WORD:

# index=name.find("mm")             #   (variable).find() function ---> shows the first occurrence of that word in the string.
# print(index)    
# print()

# index1=name.find("M")
# print(index1)
# print()



# #   7. replace() ---> (String replace):

# replace=name.replace("r","l")       # This function replace the old word with new word in the entire string. 
# print(replace)                      # (variable).replace() function ---> 'r'becomes 'l'
# print()                                    # output "Muhammadablal"

# name1="Terrible"
# print(name1.replace("r","l"))               # output Tellible
# print()

# sister="urooj"
# print(sister.replace("o","a"))              # output uraaj  
# print()



# #   8. CONVERT CASE:

# #   8.1. upper() ---> (UPPER CASE):
# my_name="Abrar"
# upper_case=my_name.upper()
# print(upper_case)
# print()

# #   8.2. lower() ---> (LOWER CASE):
# lower_case=my_name.lower()
# print(lower_case)
# print()

# """used  everywhere (user input cleaning)"""



# #  9. strip(), lstrip(), rstrip() ---> (Remove Spaces):

# text="          I am Abrar          "
# print(text.strip())                     # output ---> I am Abrar.
# print()

# print(text.lstrip())                    # output ---> I am Abrar(empty space)
# print()

# print(text.rstrip())                    # output ---> (empty space) I am Abrar
# print()


# """used  everywhere (user input, files)"""



# #   10. split() ---> (Converting String ---> List):

# print(text.split())                     # output ---> ['I','am','Abrar']
# print()

# """used in NLP, Data Processing"""



# #  11. join() ---> (Opposite of Split):

# words=["I","am","Abrar"]
# print(" ". join(words))             # Output ---> I am Abrar



# #   12. Find() vs Index():

# #   12.1 Find()
# my_name="Abrar"
# print(my_name.find("r"))            # output ---> 2


# #   12.2 index
# print(my_name.index("A"))       #output ---> 0. same as find() but shows error if not found.

# # DIFFERENCE:
# # find() ---> safe
# # Inex()---> Strict             



# #   13. isalpha(), isdigit(), isalnum():

# my_name="abrar"
# user_name="abrar123"
# pin="885522"

# print(my_name.isalpha())
# print(user_name.isalnum())
# print(pin.isdigit())

# """used in ---> Validation(Pin,phone, etc)"""



# #   14. title() ---> (capitalize each word):

# a="the end of the world"
# print(a.title())            #output ---> The End Of The World



# # 15. swapcase() ---> (Upper to lower case and vice versa):

# b="I am Abrar"
# print(b.swapcase())         # I am Abrar ---> i AM aBRAR
# print()