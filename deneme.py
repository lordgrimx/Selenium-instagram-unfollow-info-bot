import sqlite3
con = sqlite3.connect("followers.db")

cursor = con.cursor()
sorgu = "SELECT username FROM followers"
cursor.execute(sorgu)
rows = cursor.fetchall()
data_list = []
for row in rows:
    data_list.append(row)

print(data_list)