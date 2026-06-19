with open("P_6_7_file.txt","r") as f:
    content=f.readlines()

line_number=1
for line in content:
    if "python" in line.lower():
        print(f"line number {line_number}", "contains the word python")
        # line_number=line_number+1    
    else:
        print(f"in line {line_number}, word python is not found")
        # line_number=line_number+1
    line_number=line_number+1