import sqlite3

con = sqlite3.connect(r"c:\classroom\aug27\catalog.db")
print("Connected Successfully!")
con.close()