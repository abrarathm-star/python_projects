# candidate=input("Candidate: ")
# from datetime import date
# date=date.today()
# print("Dear", candidate)
# print("you are selected")
# print(date)

a=input("Candidate: ")
from datetime import date
b=date.today()
date=str(b)

letter="""Dear candidate,
You are selected.
date"""

print(letter.replace("candidate",a).replace("date",date))
