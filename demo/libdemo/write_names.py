f = open("names.txt", "at")   # Append Text

while True:
    name = input("Enter name [end to stop] :")
    if name == "end":
        break

    f.write(name + "\n")

f.close()
