import random
def game():
    return random.randint(0,1500)
score=game()
with open("high_score.txt","r") as f:
    old_score=f.read()


if old_score=="":
    old_score=0
else:
    old_score=int(old_score)
if score>old_score:
    file=open("high_score.txt","w")
    file.write(str(score))
