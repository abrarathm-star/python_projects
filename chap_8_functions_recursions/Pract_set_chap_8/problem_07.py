l1=[" abrar"," khan ","urooj","aisha ", "  arsalan "]

def remove_strip(item):
    l1.remove(item)
    print(item.strip(),"is present")

while True:
    word=input("word: ")
    for item in l1:
        if item.strip()==word:
            remove_strip(item)
            break
    else:
        print("word not found")