with open("P_01_file.txt","r") as f:
    poem=f.read()

if "twinkle" in poem.lower():
    print("word twinkle is presesnt")

else:
    print("word twinkle is not found")