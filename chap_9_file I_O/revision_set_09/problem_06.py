with open("P_6_7_file.txt","r") as f:
    text=f.read()

if "python" in text.lower():
    print("found")
else:
    print("not found")