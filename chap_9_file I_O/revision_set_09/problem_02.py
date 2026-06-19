import random
new_score=random.randint(1,2000)


with open("P_02_High_score.txt","r") as f:
    old_score=f.read()


# if old_score=="":                             # my version.
#     old_score=int(old_score.replace("","0"))          
"""or"""
if old_score=="":
    old_score=0                 
else:                               # chatGpt Version.
    old_score=int(old_score)

if int(old_score) > new_score:
    pass
elif new_score > int(old_score)     :
    with open("P_02_High_score.txt","w") as w:
        high_score=w.write(str(new_score))