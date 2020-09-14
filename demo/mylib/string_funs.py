
def has_upper(s):
    for c in s:
        if c.isupper():
            return True

    return False


def extract_upper(s):
    lst = []
    for c in s:
        if c.isupper():
            lst.append(c)

    return "".join(lst)

