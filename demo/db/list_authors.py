import sqlite3

con = sqlite3.connect(r"c:\classroom\aug27\catalog.db")
cur = con.cursor()
cur.execute("select * from authors order by fullname")
for row in cur.fetchall():
    print(f"{row[0]:3} {row[1]:20} {row[2]:30} {row[3]}")

con.close() 