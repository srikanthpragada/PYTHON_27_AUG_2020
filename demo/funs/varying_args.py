def wish(*names, message="Hi"):
    for n in names:
        print(message, n)


wish("Bill", "Steve", message="Hello")
wish("Bill", "Steve", "Mike")
