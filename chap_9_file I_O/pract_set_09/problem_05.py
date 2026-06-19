f=open("bad_words_Q5.txt","r")
text=f.read()
# print(text)
f.close()
print()

bad_words = ["abuse", "addict", "anal", "arse", "ass", "asshole", "bastard", "bitch", 
            "bloody", "blowjob", "bollocks", "boob", "bugger", "bullshit", "clit", 
            "cock", "coon", "crap", "cunt", "damn", "dick", "dildo", "dyke", 
            "fag", "faggot", "feck", "felch", "fellate", "feltch", "fuck", 
            "fucker", "hell", "homo", "jerk", "jizz", "knob", "labia", "muff", 
            "nigger", "omg", "paki", "piss", "poof", "pussy", "queer", "scrotum", 
            "shag", "shit", "slut", "spastic", "turd", "twat", "wank", "whore"]


for item in bad_words:
    if item in text:
        text=text.replace(item,"####")
print(text)

w=open("bad_words_Q5.txt","w")
w.write(text)
w.close()

