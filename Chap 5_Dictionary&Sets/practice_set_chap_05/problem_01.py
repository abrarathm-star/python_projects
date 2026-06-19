#Q.1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

a={"come":"aao", "go":"jao", "morning":"subah", "night":"raat", "day":"din",
   "fast":"tez", "slow":"aahista", "tomorrow":"kal", "day after tomorrow":"parso",
   "mine":"mera", "yours":"aapka","play":"khelna", "tall":"ooncha","long":"lambha"}

# print(len(a))


# for i in range():    #we are not using this loop function because we need an infinite program W/M software.

while True:   
   word=input("word: ")
   print(a.get(word,"not found"))  #.get() is safer than a[]. 

   """(word,"not found") will help if the word is not fund then the program will not crash."""
