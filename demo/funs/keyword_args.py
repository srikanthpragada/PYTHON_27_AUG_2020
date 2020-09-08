# Keyword arguments
def fun(**params):
    for k,v in params.items():
        print(k,v)


fun(a=10, b=20, message="Hi")
