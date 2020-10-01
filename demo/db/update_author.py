import sqlite3

con = sqlite3.connect(r"c:\classroom\aug27\catalog.db")
cur = con.cursor()
auid = input("Author Id :")
mobile = input("Mobile : ")
try:
    cur.execute("update author set mobile = ? where auid = ?", (mobile, auid))
    if cur.rowcount == 1:
        print("Updated Successfully!")
        con.commit()
    else:
        print("Author is not found!")
except Exception as ex:
    print("Sorry! Could not update author due to error!")


con.close()
