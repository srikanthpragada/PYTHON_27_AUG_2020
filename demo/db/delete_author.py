import sqlite3

con = sqlite3.connect(r"c:\classroom\aug27\catalog.db")
cur = con.cursor()
auid = input("Author Id :")
cur.execute("delete from authors where auid = ?", (auid,))
if cur.rowcount == 1:
    print("Deleted Successfully!")
else:
    print("Author Id not found!")

con.commit()
con.close()
