with open("file_Q8.txt","r") as f:
    content=f.read()

with open("copy_of_file_Q8.txt","r") as f:
    new_content=f.read()

if content==new_content:
    print("same files")
else:
    print("not same files")