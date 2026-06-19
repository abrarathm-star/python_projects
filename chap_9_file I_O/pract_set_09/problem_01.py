f=open("poem.txt","r")
text=f.read()
print(text)
f.close()
print()
while True:
    word=input("find word: ")
    if word.lower() in text.lower():
        print(f"{word} is present")
    else:
        print("word is not found")
