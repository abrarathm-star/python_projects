with open("p_4_file.txt","r") as f:
    text=f.read()

if "donkey" in text.lower():
    updated_text=text.replace("donkey","####")

w=open("p_4_file.txt","w")
w.write(updated_text)
w.close