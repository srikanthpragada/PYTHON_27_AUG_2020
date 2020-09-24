import os

files = os.walk(r"c:\classroom\aug27")

for (dirname, dirs, files) in files:
    for file in files:
        if file.endswith(".py"):
            print(dirname + "\\" + file)
