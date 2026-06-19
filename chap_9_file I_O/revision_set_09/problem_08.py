with open("P_8_file.txt","r") as f:
    text=f.read()

with open("copy_of_P_8_file.txt","a") as a:
    copied_text=a.write(text)