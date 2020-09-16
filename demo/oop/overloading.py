# Simulating overloading
# add(int,int)
# add(int,str)

def add(num, value):
    if isinstance(value, int):
        return num + value
    else: # assume value is str
        return num + int(value)


print(add(10, 20))
print(add(10, "20"))
