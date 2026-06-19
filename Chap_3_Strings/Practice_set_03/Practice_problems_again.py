print("Problem_01")

a=input("enter a name ")

greetings="Good Afternoon name."
print(greetings.replace("name",a))
print()



print("Problem_02")

letter = """Dear Name,
\tYou are selected!
\tdate"""
b=input("enter candidate name ")
from datetime import date
c=date.today().strftime("%d.%m.%y")
print(letter.replace("Name",b).replace("date",c))
print()



print("Problem_03")

intro="""My name  is Muhammad  Abrar.
I am  30 years  old.\nI  am from  pakistan.
I  have  completed  my masters  degree in  paksian."""

print("  " in intro)
print()



print("Problem_04")

print(intro.replace("  "," "))
print()



print("Problem_05")

letter1= "Dear Harry, \n\tthis python course is nice. \n\tThanks!"
print(letter1)