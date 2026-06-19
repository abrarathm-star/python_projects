with open("log_file_Q6.txt","r") as f:
    text=f.read()
print(text)
print()
number_of_python=text.lower().count("python")
if "python" in text.lower():
    print("word Python is present")
    print(number_of_python)
else:
    print("not found")