with open("P_8_file.txt","r") as f:
    text=f.read()

with open("copy_of_P_8_file.txt","r") as a:
    copied_text=a.read()

if copied_text == text:
    print("files are same")
else:
    print("file are not same")