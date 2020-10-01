import sqlite3

file = open("authors.txt", "rt")
con = sqlite3.connect(r"c:\classroom\aug27\catalog.db")
cur = con.cursor()

for line in file.readlines():
    parts = line.split(",")
    if len(parts) == 3:
        parts = list(map(str.strip, parts))
        cur.execute("insert into authors(fullname,email,mobile) values(?,?,?)", parts)

con.commit()
con.close()
