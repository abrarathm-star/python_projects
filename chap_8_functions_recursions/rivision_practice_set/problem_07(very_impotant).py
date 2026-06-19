
l=["abrAR ", " kHan ", "Shakeel ", " Urooj"]

def remove_strip():
        for item in l:
            if item.strip().lower()==word:
                print(word, "is present")
                break
        else:
             print("word not found")
while True:
    word=input("name: ")
    remove_strip()