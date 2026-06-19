#this imports the os module,which allows python to interact with the operating system(filesand folders)
import os

# thi line gets all files and folders inside the desktop directory.
files = os.listdir("C:\\Users\\Muham\\Desktop") #--- this is the directory path basicly.


# this loop goes through each item (files/folder) one by one.
for file in files:
    # this print each file name separately.
    print(file) 