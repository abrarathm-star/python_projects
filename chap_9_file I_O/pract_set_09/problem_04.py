f=open("donkey.txt","r")
text=f.read()
print(text)
f.close()
print()

replaced_word=text.replace("donkey","####")
print(replaced_word)


w=open("donkey.txt","w")
w.write(replaced_word)
w.close()