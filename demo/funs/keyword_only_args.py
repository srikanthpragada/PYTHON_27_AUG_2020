# Keyword-only arguments - n1, n2
def fun(*, n1, n2):
    pass


# fun(10, 20)  # Error
fun(n1=10, n2=20)
fun(n2=10, n1=20)
