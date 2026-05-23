import sqlite3 
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute(""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOIONCREMENT,
    name TEXT,
    age INTEGER
)
"")

conn.commit()
conn.close()

print("Database connnect successsfully!")
              