with open("P_5_file.txt","r") as f:
    text=f.read()

bad_words_list = ["ass", "bastard", "bitch", "bloody", 
                  "bollocks", "crap", "cunt", "damn", 
                  "dick", "faggot", "fuck", "hell", 
                  "jerk", "motherfucker", "nigger", 
                  "piss", "prick", "pussy", "shit", "slut"]



for item in bad_words_list:
    if item in text:
        text=text.replace(item,"####")
with open("P_5_file.txt","w") as w:
    w.write(text)
    