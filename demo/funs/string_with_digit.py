def does_not_contain_digit(st):
    for c in st:
        if c.isdigit():
            return False

    return True  # String has no digits


names = ['Java', 'Java 14', 'Python', 'SQL 99', 'JavaScript']
for s in filter(does_not_contain_digit, names):
    print(s)
