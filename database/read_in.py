import sqlite3
db = sqlite3.connect("database\profile_information.db")
cur = db.cursor()

print(cur.execute("SELECT * FROM Planes"))

def insert(table_name, values):
    cur.executemany("INSERT INTO " + table_name + " VALUES (?)", values)

# insert("Airports",[("DFW"), 
# ("LAX"),
# ("ATL"),
# ("CLT"),
# ("MIA"),
# ("BOS"),
# ("LGA"),
# ("JFK"),
# ("RDU"),
# ("SFO")])

def insert3(table_name, values):
    cur.execute("INSERT INTO " + table_name + " VALUES (?, ?, ?)", values)
    
# insert3([("Flight Type", "Domestic", "International")])
# insert3([("Pilot Roles", "Captain", "First Pilot")])
#insert("Planes", [("737"), ("787"), ("777"), ("767"), ("320")])