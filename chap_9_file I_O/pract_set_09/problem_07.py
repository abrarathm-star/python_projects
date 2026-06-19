with open("log_file_Q6.txt","r") as f:
    # text=f.read()
    # f.close()

    line_number=1
    for line in f:
        if "python" in line.lower():
            print(line_number)
            line_number=line_number+1
    
        else:
            # print("not found",end=" ")
            # print("on",line_number)
            line_number=line_number+1