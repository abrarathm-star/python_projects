with open("file_Q8.txt","r") as f:
    conent=f.read()
    print(conent)
    print()


# # w=open("copy_of_file_Q8.txt","w")
# # w.write(conent)
# # print(w)
# # w.close

with open("copy_of_file_Q8.txt","r") as f:
    new_conent=f.read()
    print(new_conent)