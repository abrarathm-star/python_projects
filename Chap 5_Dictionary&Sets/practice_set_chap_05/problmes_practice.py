# # Q.1

# a={"come":"aao", "go":"jao", "morning":"subah", "night":"raat", "day":"din",
#    "fast":"tez", "slow":"aahista", "tomorrow":"kal", "day after tomorrow":"parso",
#    "mine":"mera", "yours":"aapka","play":"khelna", "tall":"ooncha","long":"lambha"}

# while True:
#     w=input(f"word: ")
#     print(a.get(w,"not found"))
#     print()


# Q.2

# s=set()

# for i in range(8):
#     n=int(input((f"number {i+1}: ")))
#     s.update({n})                       #.update({})
#     print()
# print(s)
# print()

# """or"""

# s=set()

# for i in range(8):
#     n=int(input((f"number {i+1}: ")))
#     s.add(n)                            #.add()
#     print()
# print(s)
# print()


# Q.3

# a={18,'18'}
# print(a)

# """we do little alteration"""
# b=set()
# for i in range(2):
#     number=int(input(f"number {i+1}: "))
#     b.add(number)
# for i  in range(2):
#     word=input(f"word {2+1}: ")
#     b.add(word)
# print(b)


# # Q.4
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20')
# print(s)            # output is ---> {'20', 20}


# Q.5 

# s={}
# print(type(s))      # output is ---> <class 'dict'>


# Q.6 

# d={}

# for i in range(4):
#     friends=input(f"friend {i+1}: ")
#     lanuage=input(f"langauge {i+1}: ")
#     d[friends]= lanuage
# print(d)


# Q.7

# d={}

# for i in range(4):
#     friends=input(f"friend {i+1}: ")
#     lanuage=input(f"langauge {i+1}: ")
#     d[friends]= lanuage
# print(d)

# """ 1. dictionary does not keep the duplicate keys.
#     2. latest key replaces the old one."""



# Q.8

# d={}

# for i in range(4):
#     friends=input(f"friend {i+1}: ")
#     lanuage=input(f"langauge {i+1}: ")
#     d[friends]= lanuage
# print(d)

# """Same values(languages) are alowed in dictionaries as long as the friend(key) is different"""
