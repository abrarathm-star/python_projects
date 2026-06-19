# wipe_out=open("file_for_Q10.txt","w")
# wipe_out.write("the file content is wiped out. it was the goal of question number 10")
# wipe_out.close()

"""if you want to wipe the contents of the file again then uncquote the code above and run it, 
   the txt file will get wiped out."""


with open("file_for_Q10.txt","r") as f:
    text=f.read()
    print(text)
    print()