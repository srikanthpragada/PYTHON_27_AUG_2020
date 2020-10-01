import sqlite3

con = sqlite3.connect(r"c:\classroom\aug27\catalog.db")
cur = con.cursor()
fullname = input("Fullname    :")
email = input("Email :")
mobile = input("Mobile : ")

cur.execute("insert into authors(fullname,email,mobile) values(?,?,?)",
            (fullname, email, mobile))
print(f"Inserted {cur.rowcount} row(s)")
con.commit()
con.close()
